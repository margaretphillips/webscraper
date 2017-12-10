import requests
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/example.html")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div", {"class": "cities"})

for a in all:
    item=a.find_all("h2")
    item_str=item[0].text
    print(item_str)
