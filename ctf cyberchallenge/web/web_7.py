import requests

url = 'http://web-07.challs.olicyber.it/'

r = requests.head(url)

print(r.headers)