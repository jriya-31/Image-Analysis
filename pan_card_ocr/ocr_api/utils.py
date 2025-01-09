# ocr_api/utils.py

import cv2
import numpy as np
import pytesseract
import re
from PIL import Image

class PANCardOCR:
    @staticmethod
    def preprocess_image(image, debug=False):
        if image is None:
            raise ValueError("Invalid image data")

        # Resize if too large
        max_dimension = 1800
        height, width = image.shape[:2]
        if max(height, width) > max_dimension:
            scale = max_dimension / max(height, width)
            image = cv2.resize(image, None, fx=scale, fy=scale)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Noise removal and contrast enhancement
        denoised = cv2.bilateralFilter(gray, 9, 75, 75)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(denoised)

        # Thresholding
        thresh = cv2.adaptiveThreshold(
            enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )

        # Morphological operations
        kernel = np.ones((2, 2), np.uint8)
        opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        processed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

        if debug:
            cv2.imwrite("debug_gray.jpg", gray)
            cv2.imwrite("debug_denoised.jpg", denoised)
            cv2.imwrite("debug_enhanced.jpg", enhanced)
            cv2.imwrite("debug_thresh.jpg", thresh)
            cv2.imwrite("debug_processed.jpg", processed)

        return processed

    @staticmethod
    def extract_text(processed_image, debug=False):
        try:
            custom_config = r"--oem 3 --psm 6 -c preserve_interword_spaces=1"
            text = pytesseract.image_to_string(processed_image, config=custom_config)

            if debug:
                print(f"Raw text from Tesseract:\n{text}")

            if not text.strip():
                custom_config = r"--oem 3 --psm 4"
                text = pytesseract.image_to_string(processed_image, config=custom_config)

            return text
        except Exception as e:
            print(f"Error in text extraction: {str(e)}")
            return ""

    @staticmethod
    def parse_pan_info(text):
        patterns = {
            "pan_number": r"[A-Z]{5}[0-9]{4}[A-Z]",
            "name": r"(?i)Name\s*:\s*(.*?)(?=Father|Date|$)",
            "fathers_name": r"(?i)Father[\'s]*\s*Name\s*:\s*(.*?)(?=Date|$)",
            "dob": r"\d{2}/\d{2}/\d{4}",
        }

        extracted_info = {}
        text = text.replace("\n", " ")

        for field, pattern in patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                value = match.group(1).strip() if field in ["name", "fathers_name"] else match.group()
                extracted_info[field] = value.title() if field in ["name", "fathers_name"] else value.upper()

        return extracted_info
