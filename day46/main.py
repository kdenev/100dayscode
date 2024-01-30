import requests
from bs4 import BeautifulSoup

user_date = input("Let's go back in time baby! Type the date in this format YYYY-MM-DD") or "2010-07-28"
url = f"https://www.billboard.com/charts/hot-100/{user_date}"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
[title.getText().strip() for title in soup.find_all(name="h3", id="title-of-a-story")]