import requests

s = requests.Session()

s.get('http://web-06.challs.olicyber.it/token')
r = s.get('http://web-06.challs.olicyber.it/flag')

print(r.text)