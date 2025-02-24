#Web 08 - HTTP: una richiesta post tradizionale
import requests

url = 'http://web-08.challs.olicyber.it/login'

payload = {'username': 'admin', 'password': 'admin'}

r = requests.post(url, data=payload)

print(r.text)