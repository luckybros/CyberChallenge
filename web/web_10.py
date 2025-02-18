#Web 10 - HTTP: il metodo OPTIONS
import requests
import json

url = 'http://web-10.challs.olicyber.it/'
payload = {'key': 'value'}

r = requests.post(url, data=payload)
print("PRIMA RICHIESTA")
print(r.headers)

r = requests.put(url, data=payload)
print("SECONDA RICHIESTA")
print(r.headers)
