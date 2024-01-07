import requests
from datetime import datetime
import time
import smtplib
from email.message import EmailMessage

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_above(lat=MY_LAT, lng=MY_LONG):

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude, iss_longitude)

    if (iss_latitude-5 <= lat <= iss_latitude+5) and (iss_longitude-5 <= lng <= iss_longitude+5):
        return True
    else:
        return False

def is_it_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunrise <= time_now.hour <= sunset:
        return False
    else:
        return True
    
def send_email():
    my_email = "kdenevtest2@gmail.com"
    password = "" # <- insert password here

    msg = EmailMessage()
    msg.set_content("Go out and look at the ISS.")
    msg["Subject"] = "Look up!!!"
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


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
        
iss_tracking = True
    
while iss_tracking:
    if is_iss_above(lat=MY_LAT, lng=MY_LONG) and is_it_dark():
        print('Just look')
        send_email()
        iss_tracking = False
    time.sleep(60)
    
