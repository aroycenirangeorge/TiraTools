import pytesseract
import cv2
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe" #Tesseract_exe_address
os.environ["TESSDATA_PREFIX"] = r"D:\Program Files\Tesseract-OCR\tessdata" #tessdata_address

def run_ocr_on_prescription():
    image_path = input("Image path: ").strip()

    if not os.path.exists(image_path):
        print(f"404 at {image_path}")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("404")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
    processed = cv2.adaptiveThreshold(
        resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 41, 15
    )

    ocr_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(processed, config=ocr_config)

    print("\n------------------- OCR Result -------------------")
    print(text.strip())
    print("-------------------------------------------------")

run_ocr_on_prescription()
