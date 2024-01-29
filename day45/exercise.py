import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'

response = requests.get(url=url)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_contents = soup.find_all(name="span", class_="titleline")
article_text = [article.getText() for article in article_contents]
article_link = [article.find("a").get("href") for article in article_contents]
article_upvote = [int(span.getText().split()[0]) for span in soup.find_all(name="span", class_="score")]

most_upvoted_index = article_upvote.index(max(article_upvote))
print(article_text[most_upvoted_index], article_link[most_upvoted_index])