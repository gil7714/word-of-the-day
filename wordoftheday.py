import json
import re

from bs4 import BeautifulSoup
import requests

url = 'https://www.merriam-webster.com/word-of-the-day'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


for word in content.find_all('h2', attrs={"class": "word-header-txt"}):
    print(word.text)


definition = content.find("div", attrs={"class": "wod-definition-container"})
deftext = definition.find_next("p")
print(deftext.text)
