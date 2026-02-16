"""
Sentiment analysis using transformers (distilbert-base-uncased-finetuned-sst-2-english).
"""

from typing import Dict, Any
from transformers import pipeline as transformers_pipeline


def analyze_sentiment(transcript: Dict[str, Any]) -> Dict:
    """
    Analyze sentiment for each segment.
    
    Args:
        transcript: Transcript dict with segments
        
    Returns:
        {
            'per_segment': [{'start': float, 'end': float, 'text': str, 
                           'label': str, 'score': float}, ...]
        }
    """
    sentiment_pipe = transformers_pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=-1  # CPU
    )
    segments = transcript.get("segments", [])
    per_segment = []

    for seg in segments:
        text = seg.get("text", "")
        if not text.strip():
            continue
        # Truncate for model limit
        res = sentiment_pipe(text[:512])[0]
        per_segment.append({
            "start": seg.get("start", 0),
            "end": seg.get("end", 0),
            "text": text,
            "label": res["label"],
            "score": res["score"]
        })
    
    return {
        "per_segment": per_segment
    }

