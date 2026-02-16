# EchoEthics-ML - Complete Installation Guide

## 🎯 Quick Start (3 Steps)

### Step 1: Install Dependencies
```cmd
QUICK_INSTALL.bat
```

### Step 2: Set Hugging Face Token
```cmd
SETUP_HF_TOKEN.bat
```
Or manually:
```cmd
set HUGGINGFACE_HUB_TOKEN=your_token_here
```

### Step 3: Run the Project
```cmd
python main.py --audio data/samples/demo.wav
```

---

## 📋 Complete Installation Instructions

### Prerequisites
- ✅ Python 3.11 installed
- ✅ Windows OS
- ✅ Internet connection
- ✅ Hugging Face account (free)

### Installation Methods

#### Method 1: Automated (Recommended)
```cmd
QUICK_INSTALL.bat
```

#### Method 2: Manual Installation
```cmd
REM 1. Upgrade pip
python -m pip install --upgrade pip

REM 2. Install all dependencies
pip install -r requirements.txt

REM 3. If you get errors, run the fix script
FIX_DEPENDENCIES.bat
```

#### Method 3: Virtual Environment (Best Practice)
```cmd
REM Create virtual environment
python -m venv venv

REM Activate it
venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt
```

---

## 🔑 Hugging Face Token Setup

### Why You Need It
`pyannote.audio` requires authentication to download the speaker diarization model.

### How to Get Your Token

1. **Create Account** (if needed):
   - Visit: https://huggingface.co/join
   - Sign up for free

2. **Accept Model License**:
   - Visit: https://huggingface.co/pyannote/speaker-diarization-3.1
   - Click "Agree and access repository"

3. **Generate Token**:
   - Visit: https://huggingface.co/settings/tokens
   - Click "New token"
   - Name it (e.g., "EchoEthics-ML")
   - Copy the token

4. **Set Token**:
   ```cmd
   REM Option A: Use the setup script
   SETUP_HF_TOKEN.bat
   
   REM Option B: Set manually (temporary)
   set HUGGINGFACE_HUB_TOKEN=your_token_here
   
   REM Option C: Set permanently
   setx HUGGINGFACE_HUB_TOKEN "your_token_here"
   ```

---

## ✅ Verification

After installation, verify everything works:

```cmd
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import whisper; print('✓ Whisper OK')"
python -c "from transformers import pipeline; print('✓ Transformers OK')"
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "from core.diarization import diarize_speakers; print('✓ Diarization OK')"
python -c "import streamlit; print('✓ Streamlit OK')"
```

Expected output:
```
NumPy: 1.26.4
✓ Whisper OK
✓ Transformers OK
PyTorch: 2.2.2
✓ Diarization OK
✓ Streamlit OK
```

---

## 🐛 Troubleshooting

### Problem: NumPy version conflict
**Error**: `Numba needs NumPy 2.1 or less. Got NumPy 2.3.`

**Solution**:
```cmd
python -m pip uninstall numpy -y
python -m pip install numpy==1.26.4
```

### Problem: torch/torchvision compatibility
**Error**: `RuntimeError: operator torchvision::nms does not exist`

**Solution**:
```cmd
python -m pip uninstall torch torchvision torchaudio -y
python -m pip install torch==2.2.2 torchvision==0.17.1 torchaudio==2.2.2
```

### Problem: tokenizers version
**Error**: `tokenizers>=0.21,<0.22 is required`

**Solution**:
```cmd
python -m pip install "tokenizers>=0.21,<0.22" --upgrade --force-reinstall
```

### Problem: pyannote.audio authentication
**Error**: `401 Client Error: Unauthorized`

**Solution**:
1. Accept model license: https://huggingface.co/pyannote/speaker-diarization-3.1
2. Set token: `set HUGGINGFACE_HUB_TOKEN=your_token_here`
3. Run `SETUP_HF_TOKEN.bat` for guided setup

### Problem: Multiple dependency conflicts
**Solution**: Run the fix script
```cmd
FIX_DEPENDENCIES.bat
```

---

## 📦 Package Versions Summary

| Package | Version | Critical For |
|---------|---------|-------------|
| numpy | 1.26.4 | Whisper, numba |
| torch | 2.2.2 | pyannote.audio |
| torchvision | 0.17.1 | pyannote.audio |
| torchaudio | 2.2.2 | pyannote.audio |
| tokenizers | >=0.21,<0.22 | transformers |
| pyannote.audio | 3.1 | Speaker diarization |
| openai-whisper | 20230314 | Speech transcription |
| transformers | 4.40.1 | Sentiment analysis |
| streamlit | 1.36.0 | Web dashboard |

See `DEPENDENCY_MATRIX.md` for detailed compatibility information.

---

## 🚀 Running the Project

### Command Line Pipeline
```cmd
python main.py --audio data/samples/demo.wav
```

### Web Dashboard
```cmd
streamlit run app/dashboard.py
```
Then open http://localhost:8501 in your browser.

---

## 📚 Additional Resources

- **Full Installation Guide**: See `INSTALL.md`
- **Dependency Details**: See `DEPENDENCY_MATRIX.md`
- **Project README**: See `README.md`

---

## 💡 Tips

1. **Use Virtual Environment**: Isolates dependencies from other projects
2. **Install in Order**: NumPy → PyTorch → Others (fix script handles this)
3. **Check Versions**: After installation, verify with the verification commands
4. **Save Token**: Keep your Hugging Face token secure and accessible

---

## ✅ Installation Checklist

- [ ] Python 3.11 installed
- [ ] Dependencies installed (`QUICK_INSTALL.bat` or `pip install -r requirements.txt`)
- [ ] Hugging Face account created
- [ ] Model license accepted
- [ ] Token generated and set
- [ ] Verification tests passed
- [ ] Sample audio file added to `data/samples/demo.wav`
- [ ] Project runs successfully

---

**Need Help?** Check the troubleshooting section or review `INSTALL.md` for detailed instructions.

