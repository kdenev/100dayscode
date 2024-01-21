#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch

# Init classes
flight_data_api = FlightData()
data_api = DataManager()
flight_search_api = FlightSearch()

# Update Spreadsheet
# data_api.update_iata()

destinations_data = data_api.get_json()['prices']

for destination in destinations_data:
    flights_data = flight_search_api.get_flights(destination['iataCode'])['data']
    for flight in flights_data:
        if flight['availability']['seats'] and flight['price'] < destination['lowestPrice']:
            print(f"{destination['city']}, yes we are coming!")
            print(flight['price'], flight['local_departure'])
            # bulid the notification manager
            # send sms for first
            # send email for the all