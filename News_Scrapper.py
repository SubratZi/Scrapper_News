from datetime import date
import requests
from bs4 import BeautifulSoup

result = []

def headline_scrapper():
    beg = requests.get("https://kathmandupost.com/politics/")
    soup = BeautifulSoup(beg.content, "html.parser")
    search = soup.find_all("h3")
    search_list = list(search)
    for x in search_list:
        news_headline = str(x).replace("<h3>", "").replace("</h3>" ,"")

        news_output = "https://kathmandupost.com/politics/"

        new_news_headline = news_headline.lower() 

        updated_news_headline = new_news_headline.replace(" ","-")

        result.append (news_output + str(date.today()) +"/" +updated_news_headline )

    return result
    
for i in headline_scrapper():
    print (i)