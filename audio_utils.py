"""
Audio preprocessing and file handling utilities.
"""

import os
import librosa
import soundfile as sf
from utils.config import PROCESSED_DIR


def preprocess_audio(audio_path: str) -> str:
    """
    Converts input audio to mono 16kHz WAV and saves to processed dir.
    Returns processed audio path.
    """
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    y, sr = librosa.load(audio_path, sr=16000, mono=True)
    out_path = os.path.join(PROCESSED_DIR, "processed.wav")
    sf.write(out_path, y, 16000)
    return out_path

