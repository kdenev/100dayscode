from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


URL = "https://www.python.org"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
events_div = driver.find_element(By.CSS_SELECTOR, ".shrubbery ul")
events_li = events_div.find_elements(By.TAG_NAME, "li")
data = {}
for i in range(len(events_li)):
    time_data = events_li[i].find_element(By.TAG_NAME, "time").text
    name_data = events_li[i].find_element(By.TAG_NAME, "a").text
    data[i] = {time_data:name_data}
print(data)
driver.quit()