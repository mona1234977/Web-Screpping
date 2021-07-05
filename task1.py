import requests
from bs4 import BeautifulSoup
import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/"
n = requests.get(url)
htmlcontent = n.content
soup = BeautifulSoup(htmlcontent,"html.parser")

div=soup.find("div",class_="lister")
r=div.find("tbody",class_="lister-list")
name=r.find_all("tr")
def scrape_top_list():
    top_movie=[]
    searial_number=1
    for i in name:
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        year=i.find("td",class_="titleColumn").span.get_text()
        rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        url=i.find("td",class_="titleColumn").a["href"]
        movie_url="https://www.imdb.com"+url
        details={"Position":"","Name":"","Year":"","Rating":"","URL":""}
        details["Position"]=searial_number
        details["Name"]=movie_name
        details["Year"]=int(year[1:5])
        details["Rating"]=float(rating)
        details["URL"]=movie_url
        searial_number+=1
        top_movie.append(details.copy())
        with open("task_1.json","w") as file:
            json.dump(top_movie,file,indent=2)
screpped=scrape_top_list()