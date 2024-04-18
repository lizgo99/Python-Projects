import requests
import json
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = 90
HEIGHT_CM = 171
AGE = 24

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = os.environ["SHEET_ENDPOINT"]

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

data = {
    "query": input("Tell me wich exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
} 

nutritionix_response = requests.post(url=nutritionix_endpoint, json=data, headers=nutritionix_headers)
nutritionix_result = nutritionix_response.json()

for exercise in nutritionix_result["exercises"]:

    sheety_data = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),  
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_data, auth=('lizgo', 'Lizka!12'))
    sheety_result = sheety_response.text
    print(sheety_result)

    # print(json.dumps(sheety_result, indent=2))

