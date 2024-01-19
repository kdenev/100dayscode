import sys
import os
import requests
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator


class FlightData:
    def __init__(self) -> None:
        self.loc_api = "https://api.tequila.kiwi.com/locations/query"
        self.headers =  {"apikey": os.environ['TEQUILA_KIWI_API']}
    
    def get_iata(self, city:str):
        self.params = {
            "term": city
            , "location_type": "city"
        }
        self.response = requests.get(url=self.loc_api, params=self.params, headers=self.headers)
        self.iata = self.response.json()['locations'][0]['code']