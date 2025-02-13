import requests

r = requests.get('http://web-01.challs.olicyber.it')

print(r.text)