import sys
import os
import requests
from datetime import datetime
# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator


user_input = input("Tell what you did today: ") or "No exercises today."

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_options = {
    "query": user_input
}
headers = {
    "Content-Type":  "application/json"
    , "x-app-id": os.environ['NUTRITION_APP_ID']
    , "x-app-key": os.environ['NUTRITION_API_KEY']
}


response = requests.post(url=exercise_endpoint, json=exercise_options, headers=headers)
exercise_data = response.json()['exercises']

sheet_api = "https://api.sheety.co/820c5bec08a63ac31b81acce6cb91748/myWorkouts/workouts"
today_date = datetime.now().date().strftime("%Y/%m/%d")
today_time = datetime.now().strftime("%H:%M:%S")

headers = {
    "Authorization": os.environ['SHEETY_BEARER_WORKOUTS']
}

for e in exercise_data:
    sheet_row = {

    "workout": {
    "date": today_date,
    "time": today_time,
    "exercise": e['name'],
    "duration": e['duration_min'],
    "calories": e['nf_calories']
    }

    }

    response = requests.post(url=sheet_api, json=sheet_row, headers=headers)

