import requests

url_endpoint = 'http://localhost:8000/api/v1/'

response = requests.get(url_endpoint, json={'name': 'John', 'age': '30'},params={'name': 'Milad', 'age': '28'})

print(response.json())
