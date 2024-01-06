import smtplib
import datetime as dt
from email.message import EmailMessage
import random

now = dt.datetime.now()
week_day = now.weekday()

with open(r"day32\quotes.txt") as file:
    data = file.readlines()

my_email = "kdenevtest2@gmail.com"
password = "ndcj lgca iuip sdbu" # <- insert password here

if week_day == 5:
    msg = EmailMessage()
    msg.set_content(random.choice(data))
    msg["Subject"] = "Motivational Quote"
    msg["From"] = my_email
    msg["To"] = "kdenevgaming@gmail.com"

    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(msg)
        connection.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")