@echo off
echo ========================================
echo Quick Installation - EchoEthics-ML
echo ========================================
echo.

echo Installing packages in correct order...
echo.

echo [1/6] Installing PyTorch (2.2.1)...
python -m pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --no-deps
python -m pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1
echo ✓ PyTorch installed

echo.
echo [2/6] Installing tokenizers...
python -m pip install "tokenizers>=0.19,<0.20"
echo ✓ Tokenizers installed

echo.
echo [3/6] Installing transformers...
python -m pip install transformers==4.40.1
echo ✓ Transformers installed

echo.
echo [4/6] Installing remaining packages...
python -m pip install openai-whisper==20230314 librosa==0.10.2.post1 soundfile==0.12.1
python -m pip install pandas==2.2.2 scipy==1.13.1 matplotlib==3.8.4 plotly==5.22.0
python -m pip install streamlit==1.36.0 fpdf2==2.7.8 typing_extensions==4.12.0
echo ✓ Core packages installed

echo.
echo [5/6] Installing pyannote.audio...
python -m pip install pyannote.audio==3.1
echo ✓ pyannote.audio installed

echo.
echo [6/6] Verifying installation...
python -c "import torch; print('✓ PyTorch:', torch.__version__)"
python -c "import whisper; print('✓ Whisper OK')"
python -c "from transformers import pipeline; print('✓ Transformers OK')"
python -c "import streamlit; print('✓ Streamlit OK')"

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Next: Set Hugging Face token and test!
echo   set HUGGINGFACE_HUB_TOKEN=your_token
echo   python main.py --audio data/samples/demo.wav
echo.
pause

