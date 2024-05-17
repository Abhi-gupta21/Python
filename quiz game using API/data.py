import requests

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean&category=18")

response.raise_for_status()

data = response.json()

question_data = data['results']
