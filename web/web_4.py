import requests

url = 'http://web-04.challs.olicyber.it/users'
headers = {'Accept': 'application/xml'}
r = requests.get(url, headers=headers)

print(r.text)