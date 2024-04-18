import requests
from datetime import datetime

TOKEN = "mvkfjgnvdkfljnvlksf"
USERNAME = "lizgo"
GRAPH_ID = "graph1"

today = datetime.now()
yesterday = datetime(year=2023, month=11, day=6)

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
token_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": TOKEN,
}

user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}

token_params = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "3.0",
}

update_params = {
    "quantity": "2.0"
}



# user_response = requests.post(url=pixela_endpoint, json=user_params)
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# token_response = requests.post(url=token_endpoint, json=token_params, headers=headers)
# update_respone = requests.put(url=update_endpoint, json=update_params ,headers=headers)
delete_response = requests.delete(url=update_endpoint, headers=headers)

print(delete_response.text)