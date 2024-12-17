# setup.py
import sys
import subprocess
import platform

def install_dependencies():
    """Install project dependencies"""
    try:
        import pip
    except ImportError:
        print("pip is not installed. Please install pip first.")
        sys.exit(1)

    print("Installing dependencies...")
    
    # Determine pip command based on system
    pip_command = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    
    try:
        subprocess.check_call(pip_command)
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("Error installing dependencies. Please check your internet connection and pip installation.")
        sys.exit(1)

def check_python_version():
    """Check Python version compatibility"""
    version = platform.python_version_tuple()
    if int(version[0]) < 3 or (int(version[0]) == 3 and int(version[1]) < 8):
        print(f"Python {platform.python_version()} is not supported.")
        print("Please use Python 3.8 or newer.")
        sys.exit(1)

if __name__ == "__main__":
    check_python_version()
    install_dependencies()