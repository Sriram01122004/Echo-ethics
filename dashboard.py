"""
EchoEthics-ML Streamlit Dashboard
Refactored with model caching and robust file handling.
"""

import os
import streamlit as st
from typing import Dict, Any

from utils.config import PROCESSED_DIR
from utils.audio_utils import preprocess_audio
from core.bias_detection import analyze_bias
from core.metrics import compute_fairness_metrics
from utils.plot_utils import (
    plot_talk_times, plot_sentiment, plot_interruptions
)
from utils.report_utils import generate_pdf_report, save_json_report


# =========================
# Model Loaders (Cached)
# =========================

@st.cache_resource
def load_whisper_model():
    try:
        import whisper
        return whisper.load_model("small", device="cpu")
    except Exception as e:
        st.error(f"Failed to load Whisper model: {e}")
        raise


@st.cache_resource
def load_sentiment_pipeline():
    try:
        from transformers import pipeline
        return pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=-1
        )
    except Exception as e:
        st.error(f"Failed to load sentiment model: {e}")
        raise


@st.cache_resource
def load_diarization_pipeline():
    try:
        from pyannote.audio import Pipeline
        import torch

        token = os.getenv("HUGGINGFACE_HUB_TOKEN") or os.getenv("HF_TOKEN")

        pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            use_auth_token=token
        )
        pipeline.to(torch.device("cpu"))
        return pipeline

    except Exception as e:
        st.error(
            "⚠️ Speaker diarization requires HuggingFace authentication.\n\n"
            "1. Accept license: https://huggingface.co/pyannote/speaker-diarization-3.1\n"
            "2. Create token: https://huggingface.co/settings/tokens\n"
            "3. Set env variable: HUGGINGFACE_HUB_TOKEN"
        )
        raise


# =========================
# Processing Functions
# =========================

def transcribe_with_cached_model(audio_path: str) -> Dict[str, Any]:
    model = load_whisper_model()
    result = model.transcribe(audio_path, fp16=False)
    return {"text": result["text"], "segments": result["segments"]}


def analyze_sentiment_with_cached_model(transcript: Dict[str, Any]) -> Dict:
    pipe = load_sentiment_pipeline()
    output = []

    for seg in transcript.get("segments", []):
        text = seg.get("text", "").strip()
        if not text:
            continue
        res = pipe(text[:512])[0]
        output.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": text,
            "label": res["label"],
            "score": res["score"]
        })

    return {"per_segment": output}


def diarize_with_cached_pipeline(audio_path: str) -> list:
    pipeline = load_diarization_pipeline()
    diarization = pipeline(audio_path)

    segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "speaker": speaker,
            "start": turn.start,
            "end": turn.end
        })
    return segments


# =========================
# Dashboard
# =========================

def run_dashboard():
    st.set_page_config(page_title="EchoEthics-ML", layout="wide")
    st.title("🗣️ EchoEthics-ML — Real-time Spoken Bias Detection")

    uploaded_file = st.file_uploader(
        "🎵 Upload Meeting Audio (.wav, .mp3, ≤ 5 min)",
        type=["wav", "mp3"]
    )

    audio_path = None

    if uploaded_file:
        try:
            os.makedirs(PROCESSED_DIR, exist_ok=True)

            safe_name = uploaded_file.name.replace(" ", "_")
            audio_path = os.path.join(PROCESSED_DIR, safe_name)

            with open(audio_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.audio(audio_path)
            st.success(f"✅ Audio saved: {audio_path}")

        except Exception as e:
            st.error(f"❌ Failed to save audio: {e}")
            return

    if audio_path and st.button("🔍 Analyze Audio", type="primary"):

        if not os.path.exists(audio_path):
            st.error("❌ Uploaded audio file not found on disk.")
            return

        with st.spinner("🔄 Processing audio..."):

            # -------- Step 1: Preprocessing --------
            st.info("📝 Step 1/5: Preprocessing audio...")
            processed_audio = preprocess_audio(audio_path)

            if not processed_audio or not os.path.exists(processed_audio):
                st.error(f"❌ Processed audio file not found: {processed_audio}")
                return

            # -------- Step 2: Transcription --------
            st.info("📝 Step 2/5: Transcribing audio...")
            transcript = transcribe_with_cached_model(processed_audio)

            if not transcript.get("segments"):
                st.warning("⚠️ No speech detected.")
                return

            # -------- Step 3: Diarization --------
            st.info("👥 Step 3/5: Speaker diarization...")
            diarization = diarize_with_cached_pipeline(processed_audio)

            if not diarization:
                st.warning("⚠️ No speakers detected.")
                return

            # -------- Step 4: Bias Analysis --------
            st.info("🔍 Step 4/5: Bias analysis...")
            interactions = analyze_bias(transcript, diarization)

            # -------- Step 5: Sentiment --------
            st.info("💭 Step 5/5: Sentiment analysis...")
            sentiments = analyze_sentiment_with_cached_model(transcript)

            metrics = compute_fairness_metrics(interactions, sentiments)

            # Save reports
            json_path = os.path.join(PROCESSED_DIR, "fairness_report.json")
            save_json_report(metrics, json_path)

            # -------- Results --------
            st.header("📊 Meeting Fairness Analytics")

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Fairness Score", f"{metrics['fairness_score']:.2f}")
            c2.metric("Dominance Ratio", f"{metrics['dominance_ratio']:.2f}")
            c3.metric("Interruption Index", f"{metrics['interruption_index']:.2f}")
            c4.metric("Sentiment Balance", f"{metrics['sentiment_balance']:.2f}")

            st.subheader("📈 Visualizations")
            st.plotly_chart(plot_talk_times(metrics), use_container_width=True)
            st.plotly_chart(plot_sentiment(sentiments), use_container_width=True)
            st.plotly_chart(plot_interruptions(interactions), use_container_width=True)

            st.subheader("📄 Export")
            pdf_path = os.path.join(PROCESSED_DIR, "fairness_report.pdf")

            if st.button("📄 Generate PDF"):
                generate_pdf_report(
                    metrics,
                    [
                        plot_talk_times(metrics),
                        plot_sentiment(sentiments),
                        plot_interruptions(interactions)
                    ],
                    pdf_path
                )
                st.success("✅ PDF generated")

            with open(json_path, "r") as f:
                st.download_button(
                    "📥 Download JSON",
                    f.read(),
                    "fairness_report.json",
                    "application/json"
                )

            st.success("✅ Analysis Complete!")

    if not uploaded_file:
        st.info("👆 Upload an audio file to begin.")


if __name__ == "__main__":
    run_dashboard()
