import requests

NUM_OF_QUESTIONS = 10
QUESTION_TYPE = "boolean"

parameters = {
    "amount": NUM_OF_QUESTIONS,
    "type": QUESTION_TYPE,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]