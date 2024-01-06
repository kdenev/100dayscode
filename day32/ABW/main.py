##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
from email.message import EmailMessage
import pandas as pd
import random
import os

today = dt.datetime.now().date()
# Import data
data = pd.read_csv(r"day32\ABW\birthdays.csv")
# Create date
# data['bday'] = None
# for index, row in data.iterrows():
#     data.loc[index, "bday"] = dt.datetime(row.year, row.month, row.day).date()

def pick_random_letter():
    # Get all files in a folder
    folder_path = 'day32\\ABW\\letter_templates' 

    # List all files in the folder
    files_in_folder = os.listdir(folder_path)

    # Print the list of files
    folder_paths = ["\\".join([folder_path,file_name]) for file_name in files_in_folder]

    # Random pick
    random_letter_path = random.choice(folder_paths)

    # Read letter
    with open(random_letter_path) as file:
        letter = "".join(file.readlines())

    return letter   

def send_letter(letter, name):
    my_email = "kdenevtest2@gmail.com"
    password = "ndcj lgca iuip sdbu" # <- insert password here

    msg = EmailMessage()
    msg.set_content(letter.replace("[NAME]", name.title()))
    msg["Subject"] = "Happy Birthday!"
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

# Execute
for index,row in data.iterrows():
    if row.day == today.day and row.month == today.month:
        letter = pick_random_letter()
        print("Sending letter")
        send_letter(letter, row["name"])