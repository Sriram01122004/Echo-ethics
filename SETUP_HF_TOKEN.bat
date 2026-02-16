@echo off
echo ========================================
echo Hugging Face Token Setup
echo ========================================
echo.
echo This script helps you set up your Hugging Face token for pyannote.audio
echo.
echo Step 1: Get your token from:
echo   https://huggingface.co/settings/tokens
echo.
echo Step 2: Accept the model license at:
echo   https://huggingface.co/pyannote/speaker-diarization-3.1
echo.
echo Step 3: Enter your token below (or press Enter to skip):
set /p HF_TOKEN="Enter your Hugging Face token: "

if "%HF_TOKEN%"=="" (
    echo.
    echo No token entered. You can set it manually later with:
    echo   set HUGGINGFACE_HUB_TOKEN=your_token_here
    echo.
    pause
    exit /b 0
)

echo.
echo Setting HUGGINGFACE_HUB_TOKEN environment variable...
setx HUGGINGFACE_HUB_TOKEN "%HF_TOKEN%"
set HUGGINGFACE_HUB_TOKEN=%HF_TOKEN%

echo.
echo ✓ Token set successfully!
echo.
echo Note: The token is set for this session and permanently.
echo You may need to restart your terminal for it to take full effect.
echo.
pause

