import requests
from bs4 import BeautifulSoup
import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/"
s = requests.get(url)
htmlcontent = s.content
soup = BeautifulSoup(htmlcontent,"html.parser")

div=soup.find("div",class_="lister")
k=div.find("tbody",class_="lister-list")
name=k.find_all("tr")
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
    return movie_dic
dec_arg=group_by_year(screpped)
def group_by_decade(movies):
    moviedec = {}
    list1 = []
    for index in movies:
        mod = index%10
        decade=index-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10 = i + 9
        for x in movies:
            if x <= dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
                with open("task_3.json","w") as file:
                    json.dump(moviedec,file,indent=4)    
    return(moviedec)
pprint.pprint(group_by_decade(dec_arg))