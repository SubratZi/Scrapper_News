import requests
from bs4 import BeautifulSoup

def news_scrap():
    
    getfrom = requests.get("https://kathmandupost.com/cricket/2024/06/05/nepal-start-t20-world-cup-campaign-on-a-sour-note")
    intitial_content = BeautifulSoup(getfrom.content, "html.parser")
    search = intitial_content.find_all("p")
    contents = list(search)[0]
#     news = str(contents).replace("<p>", "").replace("</p>", "").replace("<br/>", "").replace("[","").replace("]", "").replace(",","")

#     return news

# print(news_scrap())
    return contents
print(news_scrap())