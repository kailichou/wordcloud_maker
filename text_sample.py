
from re import A
from bs4 import BeautifulSoup
import requests
from config import ARTICLE_EXAMPLE

page = requests.get(ARTICLE_EXAMPLE)
soup = BeautifulSoup(page.content,"html.parser")

container = soup.find_all("a")
paras = "\n".join([c.text for c in container])