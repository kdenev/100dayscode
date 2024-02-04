from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


URL = "https://www.amazon.se/-/en/gp/product/B0BDKL1TVX/ref=ox_sc_saved_title_5?smid=ANU9KP01APNAG&psc=1"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_decimal = driver.find_element(By.CLASS_NAME, "a-price-decimal")
print(f"The price is {price_whole.text}.{price_decimal.text}")
# driver.close()
driver.quit()

