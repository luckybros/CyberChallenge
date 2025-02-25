import requests
import json
from bs4 import BeautifulSoup, Comment

def has_comments(s):
    return(type(s) == Comment)

r = requests.get('http://web-14.challs.olicyber.it/')
soup = BeautifulSoup(r.text, 'html.parser')

result = ""

for item in soup.findAll(string=has_comments):
    print(item)