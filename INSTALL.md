# EchoEthics-ML Installation Guide

## Prerequisites

- **Python 3.11** (Windows)
- **pip** (latest version)
- **Hugging Face Account** (for pyannote.audio model access)

## Step 1: Set Up Hugging Face Token

1. Create a Hugging Face account: https://huggingface.co/join
2. Accept the model license: https://huggingface.co/pyannote/speaker-diarization-3.1
3. Generate an access token: https://huggingface.co/settings/tokens
4. Set the token as an environment variable:

   ```cmd
   set HUGGINGFACE_HUB_TOKEN=your_token_here
   ```

   Or set it permanently in Windows:
   - Open System Properties → Environment Variables
   - Add new variable: `HUGGINGFACE_HUB_TOKEN` = `your_token_here`

## Step 2: Install Dependencies

### Option A: Clean Installation (Recommended)

```cmd
REM Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install all dependencies
pip install -r requirements.txt
```

### Option B: Fix Existing Installation

If you have dependency conflicts, run the fix script:

```cmd
FIX_DEPENDENCIES.bat
```

Or manually:

```cmd
REM Step 1: Fix NumPy (critical for Whisper)
python -m pip uninstall numpy -y
python -m pip install numpy==1.26.4

REM Step 2: Fix PyTorch ecosystem
python -m pip uninstall torch torchvision torchaudio -y
python -m pip install torch==2.2.2 torchvision==0.17.1 torchaudio==2.2.2

REM Step 3: Fix tokenizers
python -m pip install "tokenizers>=0.21,<0.22" --upgrade --force-reinstall

REM Step 4: Install all requirements
pip install -r requirements.txt
```

## Step 3: Verify Installation

Run these commands to verify everything is installed correctly:

```cmd
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import whisper; print('✓ Whisper OK')"
python -c "from transformers import pipeline; print('✓ Transformers OK')"
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "from core.diarization import diarize_speakers; print('✓ Diarization OK')"
python -c "import streamlit; print('✓ Streamlit OK')"
```

## Step 4: Test the Project

1. **Add a sample audio file** to `data/samples/demo.wav`

2. **Run the pipeline:**
   ```cmd
   python main.py --audio data/samples/demo.wav
   ```

3. **Launch the dashboard:**
   ```cmd
   streamlit run app/dashboard.py
   ```

## Troubleshooting

### Issue: NumPy version conflict
**Solution:** Ensure NumPy is exactly 1.26.4 (not 2.x)
```cmd
python -m pip uninstall numpy -y
python -m pip install numpy==1.26.4
```

### Issue: torch/torchvision compatibility error
**Solution:** Reinstall matching versions
```cmd
python -m pip uninstall torch torchvision torchaudio -y
python -m pip install torch==2.2.2 torchvision==0.17.1 torchaudio==2.2.2
```

### Issue: pyannote.audio authentication error
**Solution:** 
1. Accept the model license at https://huggingface.co/pyannote/speaker-diarization-3.1
2. Set your token: `set HUGGINGFACE_HUB_TOKEN=your_token_here`

### Issue: tokenizers version error
**Solution:**
```cmd
python -m pip install "tokenizers>=0.21,<0.22" --upgrade --force-reinstall
```

## Dependency Versions Summary

| Package | Version | Notes |
|---------|---------|-------|
| NumPy | 1.26.4 | Must be <2.0 for whisper/numba |
| PyTorch | 2.2.2 | Must match torchvision |
| torchvision | 0.17.1 | Must match PyTorch |
| torchaudio | 2.2.2 | Must match PyTorch |
| pyannote.audio | 3.1 | Requires HF token |
| transformers | 4.40.1 | Requires tokenizers>=0.21 |
| tokenizers | >=0.21,<0.22 | For transformers |
| openai-whisper | 20230314 | Requires NumPy<2.0 |

## Notes

- **Virtual Environment**: Highly recommended to avoid conflicts with other projects
- **CPU-Only**: This setup is optimized for CPU inference (no GPU required)
- **Windows**: These instructions are for Windows. For Linux/Mac, adjust paths accordingly

