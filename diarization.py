"""
Speaker diarization using pyannote.audio.
"""

from typing import List, Dict
import torch

try:
    from pyannote.audio import Pipeline as PyannotePipeline
    PYANNOTE_AVAILABLE = True
except ImportError:
    PYANNOTE_AVAILABLE = False
    print("⚠️  Warning: pyannote.audio not installed. Please run: pip install pyannote.audio")


def diarize_speakers(audio_path: str) -> List[Dict]:
    """
    Perform speaker diarization on audio file.
    
    Args:
        audio_path: Path to audio file
        
    Returns:
        List of segment dicts:
        [{'speaker': 'SPEAKER_00', 'start': float, 'end': float}, ...]
    """
    if not PYANNOTE_AVAILABLE:
        raise ImportError(
            "pyannote.audio is not installed. Please install it with:\n"
            "  pip install pyannote.audio\n\n"
            "Note: You may also need to accept the model license at:\n"
            "  https://huggingface.co/pyannote/speaker-diarization-3.1"
        )
    
    # Get Hugging Face token from environment variable
    import os
    hf_token = os.getenv("HUGGINGFACE_HUB_TOKEN") or os.getenv("HF_TOKEN")
    
    try:
        pipeline = PyannotePipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            use_auth_token=hf_token
        )
    except Exception as e:
        # Fallback to older model if 3.1 not available
        try:
            pipeline = PyannotePipeline.from_pretrained(
                "pyannote/speaker-diarization",
                use_auth_token=hf_token
            )
        except Exception as e2:
            raise ImportError(
                f"Failed to load pyannote.audio pipeline. "
                f"Error: {str(e2)}\n\n"
                f"Please ensure:\n"
                f"1. You have accepted the model license at:\n"
                f"   https://huggingface.co/pyannote/speaker-diarization-3.1\n"
                f"2. Set your Hugging Face token:\n"
                f"   set HUGGINGFACE_HUB_TOKEN=your_token_here"
            )
    
    # Ensure CPU-only
    pipeline.to(torch.device("cpu"))
    diarization = pipeline(audio_path)
    
    segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "speaker": speaker,
            "start": turn.start,
            "end": turn.end
        })
    return segments

