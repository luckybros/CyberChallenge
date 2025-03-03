import requests
import json
from bs4 import BeautifulSoup

result = ""

r = requests.get('http://web-13.challs.olicyber.it/')
soup = BeautifulSoup(r.text, 'html.parser')

for item in soup.findAll('span', class_="red"):
    result += item.text

print(result)