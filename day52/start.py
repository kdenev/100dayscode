from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


import sys
import os
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.instagram.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
