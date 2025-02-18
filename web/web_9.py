#Web 09 - HTTP: una richiesta POST con body JSON
import requests
import json

url = 'http://web-09.challs.olicyber.it/login'

payload = {'username': 'admin', 'password': 'admin'}

r = requests.post(url, json=payload)

print(r.text)