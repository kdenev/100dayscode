import sys
import os
from twilio.rest import Client
from datetime import datetime, timedelta
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, data) -> None:
        self.data = data
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
        self.twilio_number = os.environ['TWILIO_NUMBER']
        self.my_number = os.environ['MY_NUMBER']

    def send_message(self):
        for destination in self.data:
            if destination['price'] != 0:
                self.body = f"""Low price alert! Only £{destination['price']} to fly from London-{destination['fly_from']} to {destination['city']}-{destination['fly_to']}, from {destination['start_date']} to {destination['end_date']}.
                """
            message = self.client.messages \
                .create(
                     body=self.body,
                     from_=self.twilio_number,
                     to=self.my_number
                 )
            print(message.status)
            # Send message only for the first one
            break        