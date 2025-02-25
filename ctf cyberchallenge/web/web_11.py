#Web 11 - HTTP: i token CSRF
import requests
import json

result = ''
s = requests.Session()

r = s.post('http://web-11.challs.olicyber.it/login', json={'username':'admin', 'password':'admin'})

for i in range(0, 4):
    csrf = r.json().get('csrf')
    r = s.get(f'http://web-11.challs.olicyber.it/flag_piece?index={i}&csrf={csrf}')
    result = result + r.json().get('flag_piece')

print(result)




