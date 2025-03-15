from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import pytesseract
from cassandra.cluster import Cluster
import hashlib
import json
from .read import identify_document, extract_data

pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\jriya\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

def connect_to_cassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('ocr_data')
    return session

@csrf_exempt
def auth(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        session = connect_to_cassandra()
        
        username = data.get('username')
        password = data.get('password')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if 'action' not in data:
            return JsonResponse({'error': 'Action required (login or register)'}, status=400)

        if data['action'] == 'register':
            check_query = "SELECT username FROM user_auth WHERE username=%s"
            rows = session.execute(check_query, [username])
            if rows.one():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            insert_query = "INSERT INTO user_auth (username, password) VALUES (%s, %s)"
            session.execute(insert_query, (username, hashed_password))
            return JsonResponse({'message': 'User registered successfully'}, status=201)

        elif data['action'] == 'login':
            query = "SELECT password FROM user_auth WHERE username=%s"
            rows = session.execute(query, [username])
            row = rows.one()
            if row and row.password == hashed_password:
                return JsonResponse({'message': 'Login successful', 'redirect_url': '/ocr-editor/'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return render(request, 'auth.html')


@csrf_exempt
def ocr_image(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image uploaded'}, status=400)

        uploaded_file = request.FILES['image']
        try:
            img = Image.open(uploaded_file)
            text = pytesseract.image_to_string(img)
            doc_type = identify_document(text)
            documents = extract_data(text, doc_type)

            return JsonResponse({'document_type': doc_type, 'documents': documents}, status=200)

        except Exception as e:
            return JsonResponse({'error': f'Error processing image: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def ocr_editor(request):
    return render(request, 'ocr_editor.html')
