import pytesseract
from PIL import Image
import os

# Set Tesseract executable path (if not in PATH)
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

# Set TESSDATA_PREFIX to tessdata folder
os.environ['TESSDATA_PREFIX'] = r"D:\Program Files\Tesseract-OCR\tessdata"

def extract_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='eng')
        return text.strip()
    except Exception as e:
        return f"Error: {e}"

# Example usage
image_path = input("Enter image path: ").strip()
print("\n🧾 Extracted Text:\n")
print(extract_text(image_path))
