@echo off
echo ========================================
echo EchoEthics-ML Quick Installation
echo ========================================
echo.

REM Check Python version
python --version
if errorlevel 1 (
    echo ERROR: Python not found! Please install Python 3.11
    pause
    exit /b 1
)

echo.
echo Step 1: Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Step 2: Installing dependencies from requirements.txt...
echo This may take several minutes...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Installation had errors. Running fix script...
    call FIX_DEPENDENCIES.bat
)

echo.
echo Step 3: Verifying critical packages...
python -c "import numpy; print('✓ NumPy:', numpy.__version__)"
python -c "import whisper; print('✓ Whisper')"
python -c "import torch; print('✓ PyTorch:', torch.__version__)"
python -c "import streamlit; print('✓ Streamlit')"

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Set your Hugging Face token: SETUP_HF_TOKEN.bat
echo 2. Add audio file to: data\samples\demo.wav
echo 3. Run: python main.py --audio data\samples\demo.wav
echo 4. Or launch dashboard: streamlit run app\dashboard.py
echo.
pause

