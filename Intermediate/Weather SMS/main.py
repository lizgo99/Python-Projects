import requests
import os
from twilio.rest import Client

# PHONE_NUMBER = "+12015523801"
    # "lat": 52.520216,
    # "lon": 13.318919,
api_key = "edf810a0dfcb86c841b516eb103896ac"
account_sid = "AC6b2273276f74ddf6f99e1308f0bf1395"
auth_token = "86a81e9c52b711055d13c6cc446c8df4"

parameters = {
    "lat": 45.5202471,
    "lon": -122.674194,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

will_rain = False

for hour in hourly_data:
    for condition in hour["weather"]:
        if int(condition["id"]) < 700:
            will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an ☔️",
                        from_='+12015523801',
                        to='+491636095447'
                    )

    print(message.status)
    