import sys
import os
import requests
from datetime import datetime, timedelta
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator


class FlightSearch:
    def __init__(self) -> None:
        self.headers =  {"apikey": os.environ['TEQUILA_KIWI_API']}
        self.url = "https://api.tequila.kiwi.com/v2/search"
        self.today = datetime.now().date()
        self.end_day = self.today + timedelta(days=180)


    def get_flights(self, city, price):
        self.params = {
            "fly_from": "city:LON"
            , "fly_to": f"city:{city}"
            , "date_from": self.today.strftime("%d/%m/%Y")
            , "date_to": self.end_day.strftime("%d/%m/%Y")
            , "price_to": price
            , "max_stopovers": 0
        }
        self.response = requests.get(url=self.url, params=self.params, headers=self.headers)
        # print(self.response.text)
        return self.response.json()