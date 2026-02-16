"""
Constants, thresholds, and model paths.
"""

import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(ROOT_DIR, "data")
SAMPLES_DIR = os.path.join(DATA_DIR, "samples")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

SAMPLE_AUDIO = os.path.join(SAMPLES_DIR, "demo.wav")
REPORT_PDF = os.path.join(PROCESSED_DIR, "fairness_report.pdf")
REPORT_JSON = os.path.join(PROCESSED_DIR, "fairness_report.json")

THRESHOLDS = {
    "dominance_warning": 1.5,
    "fairness_low": 0.5
}

