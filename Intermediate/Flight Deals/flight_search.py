import requests
from datetime import datetime, timedelta
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": "xeiFbnlOFVCHcJpdgYWRy8FCDAMI3Elk"
        }
            
    def get_destination_code(self, city_name):
        location_endpoint = f"{self.endpoint}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=self.headers, params=query)
        code = response.json()["locations"][0]["code"]
        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "one_for_city": 1,
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "USD"
        }
        
        try:
            response = requests.get(url=f"{self.endpoint}/v2/search", headers=self.headers, params=query)
            data = response.json()["data"][0]
        except IndexError:
            try:
                query["max_stopovers"] = 2
                response = requests.get(url=f"{self.endpoint}/v2/search", headers=self.headers, params=query)
                data = response.json()["data"][0]
                                
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                
                print(f"{flight_data.destination_city}: ${flight_data.price}. via stopover in {data['route'][0]['cityTo']}")
                return flight_data
                
            except:
                print(f"No flights found for {destination_city_code}.")
                return None
        else:
        
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
        


        

        