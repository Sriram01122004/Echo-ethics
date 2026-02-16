# EchoEthics-ML — Real-time Spoken Bias Detection & Mitigation

Detect, analyze, and visualize spoken bias and fairness in meetings via real-time audio analysis.

## Project Overview

EchoEthics-ML is a machine learning application that analyzes audio recordings of meetings to detect potential bias indicators such as:
- **Talk time imbalances** between speakers
- **Interruption patterns** and dominance behaviors
- **Sentiment distribution** across participants
- **Overall fairness score** based on multiple metrics

The application provides a user-friendly Streamlit dashboard for uploading audio files, viewing analysis results, and exporting detailed reports.

## Python Version Requirements

**This project requires Python 3.11.x** for compatibility with machine learning frameworks.

### Why Python 3.11?

Many ML frameworks (PyTorch, transformers, etc.) currently support Python 3.10–3.11. Python 3.11 provides:
- Stable compatibility with PyTorch 2.2.1
- Full support for transformers and related libraries
- Optimal performance for CPU-based inference

### Multiple Python Versions

You can have multiple Python versions installed on your system. This project only requires Python 3.11 for its virtual environment, not system-wide. Your system Python (including Python 3.14.2) remains unaffected.

## Installation & Setup

### 1. Verify Python 3.11

Check if Python 3.11 is available:

```bash
python3.11 --version
# or on Windows:
py -3.11 --version
```

If Python 3.11 is not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/) or use `pyenv-win`
- **macOS**: `brew install python@3.11` or use `pyenv`
- **Linux**: Use your package manager or `pyenv`

### 2. Create Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
# Windows
py -3.11 -m venv venv

# macOS/Linux
python3.11 -m venv venv
```

Activate the virtual environment:

```bash
# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

With the virtual environment activated:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Note**: Installation may take 5-10 minutes as it downloads ML models and dependencies.

### 4. Hugging Face Token (Required for Speaker Diarization)

The speaker diarization feature requires a Hugging Face token:

1. Create a Hugging Face account: https://huggingface.co
2. Accept the model license: https://huggingface.co/pyannote/speaker-diarization-3.1
3. Generate an access token: https://huggingface.co/settings/tokens
4. Set the environment variable:

```bash
# Windows (Command Prompt)
set HUGGINGFACE_HUB_TOKEN=your_token_here

# Windows (PowerShell)
$env:HUGGINGFACE_HUB_TOKEN="your_token_here"

# macOS/Linux
export HUGGINGFACE_HUB_TOKEN=your_token_here
```

For persistent setup, add this to your shell profile (`.bashrc`, `.zshrc`, etc.) or set it in your system environment variables.

## Running the Application

### Launch the Dashboard

With your virtual environment activated:

```bash
streamlit run main.py
```

The dashboard will automatically open in your browser at `http://localhost:8501`

### Using the Dashboard

1. **Upload Audio**: Click "Upload Meeting Audio" and select a `.wav` or `.mp3` file (recommended: ≤ 5 minutes)
2. **Analyze**: Click "🔍 Analyze Audio" to start processing
3. **View Results**: Review fairness metrics, visualizations, and charts
4. **Export**: Download JSON reports or generate PDF reports

## Project Structure

```
EchoEthics-ML/
├── main.py                        # Streamlit entry point (run with: streamlit run main.py)
├── requirements.txt               # Python 3.11 compatible dependencies
├── README.md                      # This file
│
├── app/
│   ├── __init__.py                # Package initialization
│   ├── dashboard.py               # Streamlit dashboard with model caching
│   └── live_feedback.py           # Optional real-time fairness feedback
│
├── core/
│   ├── __init__.py                # Package initialization
│   ├── speech_to_text.py          # Whisper transcription
│   ├── diarization.py             # Pyannote speaker separation
│   ├── bias_detection.py          # Dominance & interruption logic
│   ├── sentiment_analysis.py      # Sentiment classifier
│   └── metrics.py                 # Fairness score computation
│
├── data/
│   ├── samples/                   # Demo audio files (optional)
│   └── processed/                 # Generated transcripts, reports
│
└── utils/
    ├── audio_utils.py             # Preprocessing, file handling
    ├── plot_utils.py              # Matplotlib / Plotly helpers
    ├── report_utils.py            # PDF & JSON export
    └── config.py                  # Constants, thresholds, model paths
```

## Features

- 🎵 **Audio Upload**: Support for `.wav` and `.mp3` files via file uploader
- 📝 **Speech Transcription**: Whisper (small, CPU-only) for accurate transcription
- 👥 **Speaker Diarization**: Pyannote.audio for identifying different speakers
- 🔍 **Bias Detection**: Analyzes interruptions, dominance, and talk time distribution
- 💭 **Sentiment Analysis**: DistilBERT-based sentiment classification
- 📊 **Fairness Metrics**: Computes overall fairness score and detailed metrics
- 📈 **Visualizations**: Interactive Plotly charts for talk times, sentiment, and interruptions
- 📄 **Report Export**: Generate PDF and JSON reports
- ⚡ **Model Caching**: ML models are cached using Streamlit's `st.cache_resource` for faster subsequent runs
- 🛡️ **Error Handling**: Graceful handling of missing files, model download issues, and runtime errors

## Hardware & Performance

- **CPU-only inference** (no GPU required)
- **Audio ≤ 5 minutes** recommended for optimal performance
- **Runtime**: 30-60 seconds on modern CPU (e.g., i5 + 16 GB RAM)
- **Memory**: Requires ~4-8 GB RAM depending on audio length

## Troubleshooting

### Python Version Issues

**Problem**: `python` command doesn't point to Python 3.11

**Solution**: 
- Use `python3.11` or `py -3.11` explicitly
- Ensure virtual environment is created with Python 3.11: `py -3.11 -m venv venv`
- Verify with: `python --version` (should show 3.11.x when venv is activated)

### Installation Errors

**Problem**: `pip install` fails with dependency conflicts

**Solution**:
- Ensure you're using Python 3.11: `python --version`
- Upgrade pip: `pip install --upgrade pip`
- Try installing in a fresh virtual environment
- On Windows, you may need Visual C++ Build Tools for some packages

**Problem**: PyTorch installation fails

**Solution**:
- PyTorch is included in requirements.txt with CPU-only version
- If issues persist, install PyTorch separately: `pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu`

### Hugging Face Authentication

**Problem**: `authentication` or `token` errors during diarization

**Solution**:
1. Verify you've accepted the license: https://huggingface.co/pyannote/speaker-diarization-3.1
2. Generate a token: https://huggingface.co/settings/tokens
3. Set environment variable (see Installation step 4)
4. Restart your terminal/IDE after setting the variable
5. Verify: `echo $HUGGINGFACE_HUB_TOKEN` (Linux/Mac) or `echo %HUGGINGFACE_HUB_TOKEN%` (Windows)

### Audio Processing Issues

**Problem**: "No speech detected" or "No speakers detected"

**Solution**:
- Ensure audio file contains actual speech (not silence or music only)
- Check audio format (`.wav` or `.mp3` supported)
- Try a different audio file to verify the issue
- Audio should be at least 10-20 seconds long

**Problem**: Processing takes too long or runs out of memory

**Solution**:
- Use shorter audio files (≤ 5 minutes recommended)
- Close other applications to free up memory
- Ensure at least 8 GB RAM available
- Process audio in smaller chunks if needed

### Model Download Issues

**Problem**: Models fail to download or timeout

**Solution**:
- Check internet connection
- Some models download on first use (Whisper, transformers)
- For pyannote.audio, ensure Hugging Face token is set
- Try running again - models are cached after first download

### Streamlit Issues

**Problem**: `streamlit run main.py` fails or dashboard doesn't open

**Solution**:
- Ensure virtual environment is activated
- Verify Streamlit is installed: `pip show streamlit`
- Check for port conflicts (default: 8501)
- Try: `streamlit run main.py --server.port 8502`

### Import Errors

**Problem**: `ModuleNotFoundError` or import errors

**Solution**:
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
- Verify all `__init__.py` files exist in `app/` and `core/` directories
- Check Python path: `python -c "import sys; print(sys.path)"`

## Dependencies

Key dependencies (see `requirements.txt` for complete list):

- **torch** (2.2.1) - CPU version for ML inference
- **transformers** (4.40.1) - Hugging Face transformers for sentiment analysis
- **torchaudio** (2.2.1) - Audio processing utilities
- **openai-whisper** (20231117) - Speech-to-text transcription
- **pyannote.audio** (3.1) - Speaker diarization
- **librosa** (0.10.2) - Audio preprocessing
- **soundfile** (0.12.1) - Audio file I/O
- **streamlit** (1.36.0) - Web dashboard
- **plotly** (5.22.0) - Interactive visualizations
- **pandas**, **numpy**, **scikit-learn** - Data processing
- **matplotlib**, **seaborn** - Additional visualization

## License

This project is provided as-is for educational and research purposes.

## Contributing

Feel free to extend this project with:
- More sophisticated bias detection algorithms
- Real-time audio streaming
- Additional visualization options
- Integration with video conferencing platforms
- Support for additional audio formats

---

**Note**: This project is designed to be demo-ready and easy to understand. All core functionality is preserved while ensuring professional setup and reproducibility.
