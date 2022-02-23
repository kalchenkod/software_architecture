import requests
import json

# resp = requests.post('http://127.0.0.1:5054/facade', json={"msg": "You"})
resp = requests.get('http://127.0.0.1:5054/facade')
print(resp)