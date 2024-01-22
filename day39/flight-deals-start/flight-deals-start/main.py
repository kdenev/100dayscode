#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime
from datetime import timedelta

# Init classes
flight_data_api = FlightData()
data_api = DataManager()
flight_search_api = FlightSearch()
# Update Spreadsheet
# data_api.update_iata()

destinations_data = data_api.get_json()['prices']

for destination in destinations_data:
    flights_data = flight_search_api.get_flights(destination['iataCode'], destination['lowestPrice'])['data']
    destination['price'] = 0
    destination['start_date'] = datetime.now().date()
    destination['end_date'] = datetime.now().date()
    for flight in flights_data:
        flight_departure_date = datetime.strptime(flight['local_departure'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
        if flight['availability']['seats'] and flight['price'] < destination['lowestPrice']:
            if destination['price'] < flight['price']:
                destination['price'] = flight['price']
                destination['start_date'] = flight_departure_date
                destination['end_date'] = flight_departure_date
                destination['fly_from'] = flight['flyFrom']
                destination['fly_to'] = flight['flyTo']
            destination['start_date'] = min(destination['start_date'], flight_departure_date)
            destination['end_date'] = max(destination['end_date'], flight_departure_date)


notification_manager_api = NotificationManager(destinations_data)
notification_manager_api.send_message()