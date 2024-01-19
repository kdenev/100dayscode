#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager

fligt_api = FlightData()
data_api = DataManager()

# fligt_api.get_iata("Paris")
# print(fligt_api.iata)


# city_names = data_api.get_city_names()
# print(city_names)
data_api.update_row()