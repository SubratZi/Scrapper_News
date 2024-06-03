import requests
from bs4 import BeautifulSoup

datas = requests.get("https://kathmandupost.com/politics/")
initial_contents = BeautifulSoup(datas.content, "html.parser")
search = initial_contents.find_all("h3")
final_contents = list[search]
print(final_contents)