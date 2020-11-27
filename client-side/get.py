"""import requests
pload = {'username':'Olivia','password':'123'}
r = requests.post('http://192.168.1.121:8000',data = pload)

print(r.json())"""

import requests
from requests.auth import HTTPBasicAuth 

#res = requests.get('http://192.168.1.121:5000/todo/api/v1.0/tasks' auth=('bims', 'bims'))
res = requests.get('http://192.168.1.121:5000/todo/api/v1.0/tasks', auth = HTTPBasicAuth('bims', 'bims')) 
print(res.text)
#print(res.text)
#print(res.json())
#print(res.json)

