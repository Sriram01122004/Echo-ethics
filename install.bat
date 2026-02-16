@echo off
echo Installing EchoEthics-ML dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo.
echo Installation complete!
echo.
echo Note: If pyannote.audio fails, you may need to:
echo 1. Accept the model license at https://huggingface.co/pyannote/speaker-diarization-3.1
echo 2. Set HUGGINGFACE_HUB_TOKEN environment variable
echo.
pause

