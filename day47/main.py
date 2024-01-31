import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import sys
import os

# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator


URL = "https://www.amazon.se/-/en/gp/product/B0BDKL1TVX/ref=ox_sc_saved_title_5?smid=ANU9KP01APNAG&psc=1"
HEADERS = {
    "User-Agent": "Chrome/120.0.0.0"
    , "Accept-Language": "en,bg-BG;q=0.9,bg;q=0.8,fr;q=0.7"
}

response = requests.get(url=URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")
price = int(soup.find(name="span", class_="a-price-whole").getText()[:-1].replace(",",""))

if price < 12000:
    msg = EmailMessage()
    msg.set_content(f"Price of the camera you looking for is {price}!\nBuy Now:{URL}")
    msg["Subject"] = "Price is down"
    msg["From"] = os.environ['GMAIL_EMAIL']
    msg["To"] = os.environ['GMAIL_EMAIL']

    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=os.environ['GMAIL_EMAIL'], password=os.environ['GMAIL_API_PASS'])
        connection.send_message(msg)
        connection.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
