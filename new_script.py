from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import date
import requests
from bs4 import BeautifulSoup

app = FastAPI()

#Web_Scrapping: ------------------

result = []
def topic_scrapper():
    beg = requests.get("https://kathmandupost.com/politics/")
    soup = BeautifulSoup(beg.content, "html.parser")
    search = soup.find_all("h3")
    search_list = list(search)
    for x in search_list:
        temp = str(x)
        result.append((temp.replace("<h3>", "")).replace("</h3>" ,""))
    return result

#Creating a API: -----------------------

@app.get("/get-news/",  response_class=PlainTextResponse)

# Function: ---------------------------

def news():

    news_headline = "After broken RSP-Nepal's party head becomes prime minister\n"

    news_output = "https://kathmandupost.com/politics/"

    new_news_headline = news_headline.lower() 

    updated_news_headline = new_news_headline.replace(" ","-")

    return ( news_headline + news_output + str(date.today()) +"/" +updated_news_headline )