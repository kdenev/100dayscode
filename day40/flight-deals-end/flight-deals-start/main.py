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

# print("Welcome to Flifht Club.")
# print("We find the best flight deals and email you.")
# first_name = input("What is your first name?\n") or None
# last_name = input("What is your last name?\n") or None
# email_1 = input("What is your email?\n")
# email_2 = input("Type your eamil again.\n")

# if email_1 == email_2:
#     print("You're in the club!")
#     data_api.update_user(first_name=first_name, last_name=last_name, email=email_1)
# else:
#     print('Start again, emails do not match.')


destinations_data = data_api.get_json()['prices']

for destination in destinations_data:
    flights_data = flight_search_api.get_flights(destination['iataCode'], destination['lowestPrice'])['data']
    destination['stop_over'] = 0
    if len(flights_data) == 0:
        flights_data = flight_search_api.get_flights(destination['iataCode'], destination['lowestPrice'], stop_over=1)['data']
        destination['stop_over'] = 1
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
notification_manager_api.send_email()