from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


URL = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

cookie = driver.find_element(By.ID, "cookie")
cps = driver.find_element(By.ID, "cps")
store_items = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store div")
start_time = time.time()
last_click_time = round((time.time() - start_time))

while round(time.time() - start_time) < 5*60:

    cookie.click()

    if round((time.time() - start_time)) % 5 == 0 and round(time.time() - start_time) > 1 and round((time.time() - start_time)) != last_click_time:
        
        last_click_time = round((time.time() - start_time))
        store_items = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store div")
        
        for i in range(len(store_items)):
            try: 
                if store_items[i].get_attribute('onclick')[:3] == 'Buy':
                    money = driver.find_element(By.ID, "money")
                    price = int(store_items[i].find_element(By.TAG_NAME,'b').text.split(" - ")[1].replace(",", ""))
                    money = int(money.text.replace(",", ""))
                    if money > price:
                        continue
                    store_items[i-1].click()
                    break
            except:
                print('Element not clickable.')
                


print(f"Cookies per second: {cps.text}")
driver.quit()
