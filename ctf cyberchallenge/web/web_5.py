import requests

url = 'http://web-05.challs.olicyber.it/flag'
cookies = dict(password='admin')

r = requests.get(url, cookies=cookies)

print(r.cookies)