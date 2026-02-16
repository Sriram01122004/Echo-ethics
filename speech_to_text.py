"""
Speech-to-text transcription using Whisper (small, CPU-only).
"""

from typing import Dict, Any
import whisper


def transcribe_audio(audio_path: str) -> Dict[str, Any]:
    """
    Transcribe audio file to text using Whisper (small).
    
    Args:
        audio_path: Path to audio file
        
    Returns:
        transcript: {
            'text': str,
            'segments': [{'start': float, 'end': float, 'text': str}, ...]
        }
    """
    model = whisper.load_model("small", device="cpu")
    result = model.transcribe(audio_path, fp16=False)
    return {
        "text": result["text"],
        "segments": result["segments"]
    }

