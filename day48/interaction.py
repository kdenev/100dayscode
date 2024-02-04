from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


URL = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
aricle_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
print(aricle_count)
driver.quit()