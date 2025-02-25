import requests

payload = {'id': 'flag'}
r = requests.get('http://web-02.challs.olicyber.it/server-records', params=payload)

print(r.json)