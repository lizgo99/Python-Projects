import requests
import os

# BEARER = os.getenv("API_Bearer")
# USERNAME = os.getenv("API_Username_Sheety")

BEARER = "qweasdzxcewqdsacxz"
USERNAME = "lizgo"

PROJECT = "flightPrices"
SHEET = "users"

base_url = "https://api.sheety.co"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/261c1104ab0b4e3ff0769d50b27f7278/flightPrices"
        self.destination_data = {}
        self.headers = {
            "Authorization": f"Bearer {BEARER}",
            "Content-Type": "application/json",
        }

        
    def get_data(self):
        response = requests.get(url=f"{self.endpoint}/prices", headers=self.headers)
        self.destination_data = response.json()["prices"]
        return self.destination_data
    
    
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "prices": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.endpoint}/prices/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            
    def add_user(self, first_name, last_name, first_email):
        # endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
        # url = base_url + endpoint_url
        
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": first_email,
            }
        }
        response = requests.post(url=f"{self.endpoint}/users", json=body, headers=self.headers)
        response.raise_for_status()
        
    def get_emails(self):
        response = requests.get(url=f"{self.endpoint}/users", headers=self.headers)
        users = response.json()["users"]
        return [user["email"] for user in users]
        
        
    
    