from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cassandra.cluster import Cluster
from datetime import datetime
import json
import uuid

# Connect to Cassandra
def connect_to_cassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('ocr_data')
    return session

@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        documents = data.get('documents')

        if not user_id or not documents:
            return JsonResponse({'error': 'Username and documents required'}, status=400)

        session = connect_to_cassandra()

        query = "INSERT INTO documents (id, user_id, documents, created_at) VALUES (%s, %s, %s, %s)"
        session.execute(query, (uuid.uuid4(), user_id, json.dumps(documents), datetime.now()))

        return JsonResponse({'message': 'Data saved successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

