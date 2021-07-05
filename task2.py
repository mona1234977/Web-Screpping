import requests
from bs4 import BeautifulSoup
import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent,"html.parser")

div=soup.find("div",class_="lister")
s=div.find("tbody",class_="lister-list")
name=s.find_all("tr")
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
    return (top_movie)    
screpped=scrape_top_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        year = i["Year"]
        if year not in years:
            years.append(year)
    movie_dic = {i:[]for i in years}
    for i in movies:
        year=i["Year"]
        for x in movie_dic:
            if str(x)==str(year):
                movie_dic[x].append(i)
            with open("task_2.json","w") as file:
                json.dump(movie_dic,file,indent=4)    
    return movie_dic
group_by_year(screpped)