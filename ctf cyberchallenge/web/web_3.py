import requests

url = 'http://web-03.challs.olicyber.it/flag'
headers = {'X-Password': 'admin'}

r = requests.get(url, headers=headers)

print(r.text)