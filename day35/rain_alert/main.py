import requests
from twilio.rest import Client

api_key = "a55e8854e57b70763b35dee845725314"
account_sid = "AC3f57c2dd15f93e039187e91065d01d9f"
auth_token = "ac7bba3badba94bad675812339db268a"

url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": 41.130451
    , "lon": 14.781170
    , "appid": api_key
    , "cnt": 4
}

response = requests.get(url=url, params=params)
response.raise_for_status()
print(response.status_code)
forecast_list = response.json()['list']
will_rain = False

for f in forecast_list:
    condition_code = int(f["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True    

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella.",
                     from_='+17178379449',
                     to='+46729090744'
                 )
    
    print(message.status)