#Web 11 - HTTP: i token CSRF
import requests
import json

s = requests.Session()

r = s.post('http://web-11.challs.olicyber.it/login', json={'username':'admin', 'password':'admin'})

csrf_1 = r.json().get('csrf')

url = 'http://web-11.challs.olicyber.it/flag_piece?index=0&csrf=' + str(csrf_1)
r = s.get(f'http://web-11.challs.olicyber.it/flag_piece?index=0&csrf={csrf_1}')
print(r.text)



