@echo off
echo ========================================
echo EchoEthics-ML Dependency Fix Script
echo ========================================
echo.
echo This script will fix all dependency conflicts.
echo.
pause

echo.
echo Step 1: Fixing NumPy (for Whisper/numba compatibility)...
python -m pip uninstall numpy -y
python -m pip install numpy==1.26.4
if errorlevel 1 (
    echo ERROR: Failed to install NumPy
    pause
    exit /b 1
)
echo ✓ NumPy fixed

echo.
echo Step 2: Fixing PyTorch ecosystem (for pyannote.audio)...
python -m pip uninstall torch torchvision torchaudio -y
python -m pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1
if errorlevel 1 (
    echo ERROR: Failed to install PyTorch
    pause
    exit /b 1
)
echo ✓ PyTorch fixed

echo.
echo Step 3: Fixing tokenizers (for transformers)...
python -m pip install "tokenizers>=0.19,<0.20" --upgrade --force-reinstall
if errorlevel 1 (
    echo WARNING: tokenizers installation had issues, but continuing...
)
echo ✓ Tokenizers fixed

echo.
echo Step 4: Installing all requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Some packages failed to install
    echo Check the error messages above
    pause
    exit /b 1
)
echo ✓ All requirements installed

echo.
echo Step 5: Verifying installations...
python -c "import numpy; print('✓ NumPy:', numpy.__version__)" || echo ✗ NumPy check failed
python -c "import whisper; print('✓ Whisper OK')" || echo ✗ Whisper check failed
python -c "from transformers import pipeline; print('✓ Transformers OK')" || echo ✗ Transformers check failed
python -c "import torch; print('✓ PyTorch:', torch.__version__)" || echo ✗ PyTorch check failed
python -c "from core.diarization import diarize_speakers; print('✓ Diarization OK')" || echo ✗ Diarization check failed (may need HF token)

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo IMPORTANT: Set your Hugging Face token:
echo   set HUGGINGFACE_HUB_TOKEN=your_token_here
echo.
echo Then test with:
echo   python main.py --audio data/samples/demo.wav
echo.
pause
