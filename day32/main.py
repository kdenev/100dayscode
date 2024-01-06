# import smtplib
# from email.message import EmailMessage

# my_email = "kdenevtest2@gmail.com"
# password = "" # <- insert password here

# msg = EmailMessage()
# msg.set_content("Test message")
# msg["Subject"] = "Test Email"
# msg["From"] = my_email
# msg["To"] = "kdenevgaming@gmail.com"

# try:
#     connection = smtplib.SMTP("smtp.gmail.com", 587)
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.send_message(msg)
#     connection.quit()
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Failed to send email. Error: {e}")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1992, month=7, day=28, hour=12, minute=45)
print(date_of_birth)