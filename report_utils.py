"""
Helpers for PDF and JSON report export.
"""

import json
import os
from typing import Dict, List, Any
from fpdf import FPDF


def save_json_report(metrics: Dict[str, Any], json_path: str) -> None:
    """Save metrics to a JSON file."""
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w") as f:
        json.dump(metrics, f, indent=2)


def generate_pdf_report(metrics: Dict[str, Any], figures: List[Any], pdf_path: str) -> None:
    """Generate a PDF report with metrics and charts."""
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "EchoEthics-ML Fairness Report", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    
    pdf.ln(5)
    pdf.cell(0, 10, f"Fairness Score: {metrics['fairness_score']:.2f}", ln=True)
    pdf.cell(0, 10, f"Dominance Ratio: {metrics['dominance_ratio']:.2f}", ln=True)
    pdf.cell(0, 10, f"Interruption Index: {metrics['interruption_index']:.2f}", ln=True)
    pdf.cell(0, 10, f"Sentiment Balance: {metrics['sentiment_balance']:.2f}", ln=True)
    
    pdf.ln(5)
    pdf.cell(0, 10, "Talk Times:", ln=True)
    for spk, t in metrics["talk_times"].items():
        pdf.cell(0, 10, f"  {spk}: {t:.1f} s", ln=True)
    
    pdf.ln(5)
    pdf.cell(0, 10, "See dashboard for full charts.", ln=True)
    pdf.output(pdf_path)

