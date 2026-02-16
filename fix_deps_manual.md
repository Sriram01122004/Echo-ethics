# Manual Dependency Fix Instructions

The automatic fix didn't work due to dependency conflicts. Please run these commands **manually** in your terminal:

## Step 1: Fix NumPy (Critical for Whisper)
```cmd
python -m pip uninstall numpy -y
python -m pip install "numpy==1.26.4"
```

## Step 2: Fix Tokenizers (Critical for Transformers)
```cmd
python -m pip install "tokenizers>=0.21,<0.22" --upgrade --force-reinstall
```

## Step 3: Verify
```cmd
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import whisper; print('✓ Whisper OK')"
python -c "from transformers import pipeline; print('✓ Transformers OK')"
```

## Step 4: Fix Torch/Torchvision (if pyannote.audio fails)
```cmd
python -m pip uninstall torch torchvision torchaudio -y
python -m pip install torch==2.2.2 torchvision==0.17.1 torchaudio==2.2.2
```

## Alternative: Use a Virtual Environment (Recommended)

Create a clean environment to avoid conflicts:

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

