import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'

response = requests.get(url=url)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_contents = soup.find(name="span", class_="titleline")
article_text = article_contents.getText()
article_link = article_contents.find("a").get("href")
article_upvote = soup.find(name="span", class_="score").getText()