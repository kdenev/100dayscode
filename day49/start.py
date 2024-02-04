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

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3816696614&f_AL=true&f_TPR=r604800&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

sign_in_xpath = "/html/body/div[3]/header/nav/div/a[2]"
submit_xpath = """//*[@id="organic-div"]/form/div[3]/button"""

##################### Log in ########################
time.sleep(.5)
sign_in_button = driver.find_element(By.XPATH, sign_in_xpath)
sign_in_button.click()

time.sleep(.5)
email = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.XPATH, submit_xpath)

email.send_keys(os.environ['LINKEDIN_EMAIL'])
password.send_keys(os.environ['LINKEDIN_PASSWORD'])
submit_button.click()
#####################################################

################### Get Job Cards ###################

# close_chat_xpath = """//header/div/svg[@data-test-icon="chevron-down-small"]"""
job_card_xpath = """//div[@data-view-name="job-card"]"""

# close_chat_button = driver.find_element(By.XPATH, close_chat_xpath)
# close_chat_button.click()
time.sleep(2)
job_cards = driver.find_element(By.XPATH, """//div[@data-results-list-top-scroll-sentinel]""").find_elements(By.XPATH, job_card_xpath)

for card in job_cards:
    card.click()
    time.sleep(1)
    apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
    apply_button.click()
    time.sleep(1)
    try:
        submit_app_xpath = """//button[@aria-label="Submit application"]"""
        submit_button_app = driver.find_element(By.XPATH, submit_app_xpath)
        print(submit_button_app.get_attribute('innerHTML'))
        driver.find_element(By.XPATH, """//div[@data-test-modal-id="easy-apply-modal"]/div/button[@aria-label="Dismiss"]""").click()
        time.sleep(.5)
        driver.find_element(By.XPATH, """//div[@data-test-modal-id="data-test-easy-apply-discard-confirmation"]/div/div/button[@data-control-name="discard_application_confirm_btn"]""").click()
    except:
        driver.find_element(By.XPATH, """//div[@data-test-modal-id="easy-apply-modal"]/div/button[@aria-label="Dismiss"]""").click()
        time.sleep(.5)
        driver.find_element(By.XPATH, """//div[@data-test-modal-id="data-test-easy-apply-discard-confirmation"]/div/div/button[@data-control-name="discard_application_confirm_btn"]""").click()
        continue

time.sleep(10)
driver.quit()