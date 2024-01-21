import sys
import os
import requests
from flight_data import FlightData
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
        # Get the data
        self.data = self.get_json()
        # Init the FlighData
        self.flight_data = FlightData()
        
    def get_json(self):
        '''
            Returns the whole spreadsheet data in json format.
        '''
        self.response = requests.get(url=self.sheety_api, headers=self.headers)
        self.response_code = int(self.response.status_code)
        # print(self.response.text)
        if self.response_code >= 400 and self.response_code < 500:
            return None
        return self.response.json()
    
    def update_row(self, row:int=2, value:str=None):
        '''
            Updates the iata code for the provided inputs.
        '''
        self.json = {
            "price":{
                "iataCode": value
            }
        }
        self.response = requests.put(url=self.sheety_api+f"/{row}", headers=self.headers, json=self.json)

    def update_iata(self):
        '''
            Updates the iata code for the whole spreasheet 
            looping through all the rows.
        '''
        for city in self.data['prices']:
            # Fetcg iata code using the FlightData class
            city['iataCode'] = self.flight_data.get_iata(city['city'])
            # Updata row information
            self.update_row(row=city['id'], value=city['iataCode'])