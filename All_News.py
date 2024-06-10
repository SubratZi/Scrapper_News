from datetime import date
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
def newslink_scrapper():

    fetch = requests.get("https://kathmandupost.com/politics/")
    soup = BeautifulSoup(fetch.content, "html.parser")
    trending_topics_list = soup.select(".trending-topics-list  a[href]")
    global Scrapped_link
    Scrapped_link = []
    for link in trending_topics_list:
        Scrapped_link.append(link["href"])
    return Scrapped_link

news_link = newslink_scrapper()

newslink_dict = {}

def news_report():

    for y in news_link:
        url = "https://kathmandupost.com" + y
        getnews = requests.get(url)
        soup_1 = BeautifulSoup(getnews.content, "html.parser")
        news = soup_1.select(".story-section p")
        newslink_dict[url] = news
    return newslink_dict

extracted_content = news_report()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def news_content():
    return templates.TemplateResponse("index.html",(str(extracted_content)))