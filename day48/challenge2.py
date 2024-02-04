from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


URL = "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

fname.send_keys("K")
lname.send_keys("D")
email.send_keys("kd@gmail.com")
email.send_keys(Keys.ENTER)

