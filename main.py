import requests
import os
from datetime import datetime


API_ID = os.environ["nutri_api_ID"]
API_KEY = os.environ["nutri_api_key"]

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exercise_text = input("Tell me what exercises you did: ")

exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 90.72,
    "height_cm": 187.96,
    "age": 22
}

response = requests.post(url=url, json=exercise_params, headers = headers)
result = response.json()
print(result)

today = datetime.now()


formatted_date = today.strftime("%m/%d/%Y")
formatted_time = today.strftime("%H:%M:%S")

sheety_url = "https://api.sheety.co/ea3ed7eba60791731d14bf1ec05768a8/myWorkouts/workouts"

headers = {
    "Authorization": os.environ["sheety_auth"]
}
for exercise in result["exercises"]:
    sheety_data = {
        "workout" : {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"] 
        }
    }

    response = requests.post(url=sheety_url, json=sheety_data, headers=headers)
    print(response.status_code)