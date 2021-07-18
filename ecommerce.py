import requests
from bs4 import BeautifulSoup
import pprint
import json

def scrap_data():
    url="https://webscraper.io/test-sites"
    r=requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent,"html.parser")
    div=soup.find_all("div",class_= "col-md-7 pull-right" )
    d=[]
    srno=1
    for i in div:
        name=i.find("h2",class_="site-heading").get_text()
        url=i.find("h2",class_="site-heading").a["href"]
        url1_="https://webscraper.io/test-sites"+url
        print(url1_)
        print(name)

        
        
scrap_data()