"""
Compute fairness/relevant meeting metrics and score.
"""

from typing import Dict, Any


def compute_fairness_metrics(interactions: Dict, sentiments: Dict) -> Dict[str, Any]:
    """
    Computes dominance ratio, interruption index, sentiment balance, and overall fairness score.
    
    Args:
        interactions: Bias analysis results
        sentiments: Sentiment analysis results
        
    Returns:
        Metrics dict with fairness score and all computed metrics
    """
    speakers = list(interactions.get("speakers", []))
    talk_times = interactions.get("talk_times", {})
    interruptions = interactions.get("interruptions", {})
    total_talk = sum(talk_times.values()) or 1

    # Dominance: max talktime ratio over mean
    if len(talk_times) > 0:
        mean_talk = total_talk / len(talk_times)
        dom_ratios = {spk: talk_times[spk] / mean_talk for spk in speakers}
        max_dom = max(dom_ratios.values()) if dom_ratios else 1.0
        dominance_ratio = max_dom
    else:
        dominance_ratio = 1.0

    # Interruption index: max per-person
    total_interrupts = sum(interruptions.values()) or 1
    if total_interrupts > 0:
        int_ratios = {spk: interruptions.get(spk, 0) / total_interrupts for spk in speakers}
        max_int = max(int_ratios.values()) if int_ratios else 0.0
        interruption_index = max_int
    else:
        interruption_index = 0.0

    # Sentiment: ratio of positive to negative
    segs = sentiments.get("per_segment", [])
    if len(segs) > 0:
        pos_count = sum(1 for s in segs if s.get("label") == "POSITIVE")
        neg_count = sum(1 for s in segs if s.get("label") == "NEGATIVE")
        sentiment_balance = (pos_count - neg_count) / len(segs)
    else:
        sentiment_balance = 0.0

    # Fairness score: aggregate normalized
    # Lower dominance/interruption, higher sentiment → higher fairness
    fairness_score = max(
        0.0,
        1.0
        - 0.4 * (dominance_ratio - 1)
        - 0.4 * interruption_index
        + 0.2 * sentiment_balance,
    )
    fairness_score = min(1.0, max(0.0, fairness_score))

    return {
        "speakers": speakers,
        "talk_times": talk_times,
        "dominance_ratio": dominance_ratio,
        "interruption_index": interruption_index,
        "sentiment_balance": sentiment_balance,
        "fairness_score": fairness_score,
    }

