#Web 12 - Tecnologie web: estrarre semplici contenuti da una pagina web
import requests
import json
from bs4 import BeautifulSoup

r = requests.get('http://web-12.challs.olicyber.it/')
soup = BeautifulSoup(r.text, 'html.parser')

for item in soup.find_all('p'):
    print(item)
