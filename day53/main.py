from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

import sys
import os
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--user-data-dir=c:/Users/K/AppData/Local/Google/Chrome/User Data/")
chrome_options.add_argument("--no-sandbox")

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdCZLpN-Ha9D0wTA7aT5xIn1Gkl0pD_1p3_okIrgaPC75Ph4g/viewform?usp=sf_link"
RESPONSES_URL = "https://docs.google.com/forms/d/168V6iarfHtp5hb0TS-SDQY-RfAksPSc0VKr0mRAh28c/edit?pli=1#responses"
WEB_URL = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(WEB_URL)
soup = BeautifulSoup(response.text, "html.parser")

anchor_list = soup.find(name="div", id="grid-search-results").find_all(name="a", class_="property-card-link")
price_list = soup.find(name="div", id="grid-search-results").find_all(name="span", attrs={'data-test':'property-card-price'})
address_list = soup.find(name="div", id="grid-search-results").find_all(name="address")

links = [link.get("href") for link in anchor_list]
prices = [price.getText().split("+")[0].replace("/mo", "") for price in price_list]
addresses = [address.getText().strip() for address in address_list]

driver = webdriver.Chrome(options=chrome_options)

for link, price, address in zip(links, prices, addresses):
    driver.get(url=FORM_URL)
    time.sleep(.5)
    driver.find_element(By.XPATH, """//input[@aria-labelledby="i1"]""").send_keys(address)
    driver.find_element(By.XPATH, """//input[@aria-labelledby="i5"]""").send_keys(price)
    driver.find_element(By.XPATH, """//input[@aria-labelledby="i9"]""").send_keys(link)
    driver.find_element(By.XPATH, """//span[text()="Submit"]""").click()
    time.sleep(1)
    break

driver.get(url=RESPONSES_URL)
time.sleep(.5)
driver.find_element(By.XPATH, """//span[text()="Link to Sheets"]""").click()
time.sleep(.5)
driver.find_element(By.XPATH, """//span[text()="Create"]""").click()
time.sleep(1)

driver.quit()