import requests
from bs4 import BeautifulSoup
import pprint
import json
def pickle():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    m = requests.get(url)
    # htmlcontent = m.content
    Soup = BeautifulSoup(m.text,"html.parser")
    Page_div=Soup.find("div",class_="_1gX7")
    P_num=Page_div.span.get_text()
    s_list=P_num.split(" ")
    a=int(s_list[1])
    c=a//32+1
    pickle=[]
    searial_number=1
    i=1
    while i<=c:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
        m = requests.get(url)
        soup = BeautifulSoup(m.text,"html.parser")
        div = Soup.find("div",class_="_3RA-")
        b = div.find_all("div",class_="UGUy")
        b1 = div.find_all("div",class_="_1kMS")
        b2 = div.find_all("div",class_="_3WhJ")
        j=0
        while j<len(b):
            Pickle_name=b[i].get_text()
            Pickle_price=b1[i].get_text()
            Pickle_link=b2[i].a["href"]
            m="https://paytmmall.com/"+Pickle_link
            dict={"Name":"","Price":"","Url":"","Position":"task2.py"}
            dict["Name"]=Pickle_name
            dict["Price"]=Pickle_price
            dict["Url"]=Pickle_link
            dict["Position"]=searial_number
            pickle.append(dict.copy())

            searial_number+=1
            j+=1
        i+=1
    with open("task_4.json","w") as file:
        json.dump(pickle,file,indent=4)
print(pickle())