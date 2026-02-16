"""
Setup script to install all dependencies for EchoEthics-ML
"""

import subprocess
import sys

def install_requirements():
    """Install all requirements from requirements.txt"""
    print("Installing dependencies from requirements.txt...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✓ All dependencies installed!")

if __name__ == "__main__":
    install_requirements()

