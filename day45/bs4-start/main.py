from bs4 import BeautifulSoup

with open(r"day45\bs4-start\website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_anchor_tags = soup.find_all(name='a')

for tag in all_anchor_tags:
    # print(tag.getText())
    tag.get("href")


heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)
print(section_heading.value)


company_url = soup.select_one(selector="p a")
name_url = soup.select_one(selector="#name")
heading = soup.select(selector=".heading")
print(company_url)
