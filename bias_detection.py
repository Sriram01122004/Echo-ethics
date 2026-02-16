"""
Bias logic: interruptions, dominance, and interaction analytics.
"""

from typing import Dict, List, Any


def analyze_bias(transcript: Dict[str, Any], diarization: List[Dict]) -> Dict:
    """
    Analyze interruptions and dominance per speaker.
    
    Args:
        transcript: Transcript dict with segments
        diarization: List of speaker segments with start/end times
        
    Returns:
        {
            'speakers': set([...]),
            'talk_times': {speaker: seconds},
            'interruptions': {speaker: count},
            'interruption_pairs': {(A,B): count},  # who interrupts whom
        }
    """
    talk_times = {}
    interruptions = {}
    interruption_pairs = {}
    speakers = set()

    # Calculate talk times per speaker
    diarization_sorted = sorted(diarization, key=lambda seg: seg["start"])
    for seg in diarization_sorted:
        spk = seg["speaker"]
        dur = seg["end"] - seg["start"]
        talk_times[spk] = talk_times.get(spk, 0) + dur
        speakers.add(spk)

    # Compute interruptions (change of speaker within small gap)
    min_gap = 0.7  # seconds
    for i in range(1, len(diarization_sorted)):
        prev = diarization_sorted[i - 1]
        curr = diarization_sorted[i]
        gap = curr["start"] - prev["end"]
        if 0 <= gap < min_gap and prev["speaker"] != curr["speaker"]:
            # interruption detected
            inter = curr["speaker"]
            target = prev["speaker"]
            interruptions[inter] = interruptions.get(inter, 0) + 1
            key = (inter, target)
            interruption_pairs[key] = interruption_pairs.get(key, 0) + 1

    return {
        "speakers": speakers,
        "talk_times": talk_times,
        "interruptions": interruptions,
        "interruption_pairs": interruption_pairs,
    }

