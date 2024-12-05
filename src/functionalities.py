import requests

BASE_URL = 'http://localhost:8000'

def check_health():
    response = requests.get(BASE_URL + '/health')
    return response.json()

def upload_file(file_path: str) -> dict:
    with open(file_path, 'rb') as f:
        response = requests.post(BASE_URL + '/upload_file', files={'file': f})
    return response.json()

def query_files(query: str) -> str:
    response = requests.get(BASE_URL + '/api/v1/query', params={'q': query, 'csv': True})
    return response.json().get('result')