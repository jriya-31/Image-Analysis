from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cassandra.cluster import Cluster
import json

def connect_to_cassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('ocr_data')
    return session

@csrf_exempt
def get_data(request, user_id):
    session = connect_to_cassandra()
    query = "SELECT * FROM documents WHERE user_id=%s"
    rows = session.execute(query, [user_id])

    data = []
    for row in rows:
        data.append({
            "id": str(row.id),
            "documents": json.loads(row.documents),  
            "created_at": row.created_at
        })

    if data:
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'No data found'}, status=404)

