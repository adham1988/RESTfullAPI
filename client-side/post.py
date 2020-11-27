import requests
from requests.auth import HTTPBasicAuth 
a = 71
data = {"rule": a}
response = requests.post('http://192.168.1.163:5000/todo/api/v1.0/tasks', auth = HTTPBasicAuth('bims', 'bims'), json={"rule": a})
print(response.status_code)
