import sys
import os
import requests
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator


class DataManager:
    def __init__(self) -> None:
        self.sheety_api = "https://api.sheety.co/820c5bec08a63ac31b81acce6cb91748/flightDeals/prices"
        self.headers = {
            "Authorization": os.environ['SHEETY_BEARER_WORKOUTS']
        } 
        self.response_code = 200
        
    def get_city_names(self):
        self.response = requests.get(url=self.sheety_api, headers=self.headers)
        self.response_code = int(self.response.status_code)
        print(self.response.text)
        if self.response_code >= 400 and self.response_code < 500:
            return None
        return [row["city"] for row in self.response.json()["prices"]]
    def update_row(self, row:int=2, value:str=None):
        self.json = {
            "price":{
                "iataCode": "TEX"
            }
        }
        self.response = requests.put(url=self.sheety_api+f"/{row}", headers=self.headers, json=self.json)