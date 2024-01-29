import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

file =  open(r'day45\Starting Code - 100 movies to watch start\titles.txt', 'w', encoding='utf-8')
file.write("\n".join(titles[::-1]))