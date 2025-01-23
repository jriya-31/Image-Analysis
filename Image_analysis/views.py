from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import pytesseract
from .read import identify_document,extract_data,format_data
pytesseract.pytesseract.tesseract_cmd = r"c:\\Users\\jriya\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

@csrf_exempt
def ocr_image(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image uploaded'}, status=400)

        uploaded_file = request.FILES['image']
        try:
            img = Image.open(uploaded_file)
            text = pytesseract.image_to_string(img)
            type=identify_document(text)
            extracted_data=extract_data(text,type)
            res=format_data(extracted_data)
            return JsonResponse({'text': res}, status=200)
        except Exception as e:
            return JsonResponse({'error': f'Error processing image: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
