from datetime import date
import requests
from bs4 import BeautifulSoup

def newslink_scrapper():

    beg = requests.get("https://kathmandupost.com/politics/")
    soup = BeautifulSoup(beg.content, "html.parser")
    trending_topics_list = soup.select(".trending-topics-list  a[href]")
    global head
    head = []
    for link in trending_topics_list:
        head.append(link["href"])
    return head

a = newslink_scrapper()

newslink_dict = {}

x = ["news_1","news_2 ", "news_3","news_4","news_5","news_6"]

for i,y in zip(x,a):
    url = "https://kathmandupost.com" + y
    newslink_dict[i] = url
print(newslink_dict)












   