import os
from PIL import Image
import pytesseract
import subprocess

# Path to your shell script
script_path = "./bash/screenshot.sh"


def getScreenshot():
    # Call the script
    subprocess.run(["bash", script_path], check=True)

def getTextFromImage():
    image_path = "/home/serii/Downloads/screen.jpg"
    image = Image.open(image_path)  # Replace with your screenshot path
    gray = image.convert('L')
    text = pytesseract.image_to_string(gray)
    print(text)
    # remove image from system
    os.remove(image_path)

def extractTextFromImage():
    getScreenshot()
    getTextFromImage()
