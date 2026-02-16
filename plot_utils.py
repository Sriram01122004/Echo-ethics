"""
Plotting helpers using Plotly or Matplotlib.
"""

import plotly.graph_objs as go
from typing import Dict, List, Any


def plot_talk_times(metrics: Dict[str, Any]) -> go.Figure:
    """Plot talk time per speaker as a bar chart."""
    talk_times = metrics["talk_times"]
    speakers = list(talk_times.keys())
    values = [talk_times[spk] for spk in speakers]
    fig = go.Figure([go.Bar(
        x=speakers, 
        y=values, 
        text=[f"{v:.1f}s" for v in values], 
        textposition="auto"
    )])
    fig.update_layout(title="Talk Time per Speaker", yaxis_title="Seconds")
    return fig


def plot_sentiment(sentiments: Dict[str, Any]) -> go.Figure:
    """Plot sentiment distribution as a pie chart."""
    per_segment = sentiments.get("per_segment", [])
    pos = sum(1 for s in per_segment if s.get("label") == "POSITIVE")
    neg = sum(1 for s in per_segment if s.get("label") == "NEGATIVE")
    fig = go.Figure(go.Pie(
        labels=["Positive", "Negative"],
        values=[pos, neg],
        hole=0.3
    ))
    fig.update_layout(title="Sentiment Distribution")
    return fig


def plot_interruptions(interactions: Dict[str, Any]) -> go.Figure:
    """Plot interruptions between speakers."""
    pairs = interactions.get("interruption_pairs", {})
    if not pairs:
        fig = go.Figure()
        fig.add_annotation(
            text="No Interruptions Detected",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        fig.update_layout(title="Interruptions Between Speakers")
        return fig
    
    fig = go.Figure(go.Bar(
        x=[f"{a}→{b}" for (a, b) in pairs.keys()],
        y=list(pairs.values()),
        text=list(pairs.values()), 
        textposition='auto'
    ))
    fig.update_layout(title="Interruptions Between Speakers", yaxis_title="Count")
    return fig


def plot_all(metrics: Dict[str, Any], interactions: Dict[str, Any], sentiments: Dict[str, Any]) -> List[go.Figure]:
    """Generate all plots for the report."""
    return [
        plot_talk_times(metrics),
        plot_sentiment(sentiments),
        plot_interruptions(interactions),
    ]

