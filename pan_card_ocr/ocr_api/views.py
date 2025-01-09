# ocr_api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import PANCardOCR
import cv2
import numpy as np
import os
import logging

logger = logging.getLogger(__name__)

class PANCardOCRView(APIView):
    def post(self, request):
        try:
            if "image" not in request.FILES:
                return Response(
                    {"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST
                )

            image_file = request.FILES["image"]
            valid_extensions = [".jpg", ".jpeg", ".png", ".tiff", ".bmp"]
            ext = os.path.splitext(image_file.name)[1].lower()

            if ext not in valid_extensions:
                return Response(
                    {"error": f"Invalid file format. Supported formats: {', '.join(valid_extensions)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if image_file.size > 4 * 1024 * 1024:
                return Response(
                    {"error": "File size too large. Maximum size is 4MB"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            image_bytes = image_file.read()
            nparr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            ocr = PANCardOCR()
            processed_image = ocr.preprocess_image(image, debug=True)
            text = ocr.extract_text(processed_image, debug=True)
            pan_info = ocr.parse_pan_info(text)

            if not pan_info:
                return Response(
                    {"error": "Could not extract information from image"},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )

            pan_info.update({"raw_text": text, "success": True, "message": "PAN card information extracted successfully"})
            return Response(pan_info, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error during PAN card OCR processing: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
