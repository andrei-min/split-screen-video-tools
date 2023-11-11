import subprocess
import platform
import os
import requests
import zipfile

def is_ffmpeg_installed():
    try:
        # Run the command to check if ffmpeg is installed
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_ffmpeg(install_dir):
    system = platform.system().lower()

    if system == 'darwin':
        # macOS (using Homebrew)
        subprocess.run(['brew', 'install', 'ffmpeg'], check=True)
    elif system == 'linux':
        # Linux (assuming a Debian-based system using apt)
        subprocess.run(['sudo', 'apt', 'install', 'ffmpeg'], check=True)
    elif system == 'windows':
        # Windows
        download_url = 'https://ffmpeg.org/download.html'
        download_path = 'ffmpeg.zip'

        # Download ffmpeg zip file
        response = requests.get(download_url)
        with open(download_path, 'wb') as zip_file:
            zip_file.write(response.content)

        # Extract the zip file
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(install_dir)

        # Add ffmpeg directory to PATH
        os.environ['PATH'] += os.pathsep + os.path.join(install_dir, 'bin')

        print("ffmpeg installation successful.")
    else:
        print("Unsupported operating system. Please install ffmpeg manually.")

if __name__ == "__main__":
    if is_ffmpeg_installed():
        print("ffmpeg is already installed.")
    else:
        install_dir = input("Enter the installation directory for ffmpeg (e.g., C:\\ffmpeg): ")
        print("ffmpeg not found. Attempting to install...")
        install_ffmpeg(install_dir)
        if is_ffmpeg_installed():
            print("ffmpeg installation successful.")
        else:
            print("Failed to install ffmpeg. Please install it manually.")