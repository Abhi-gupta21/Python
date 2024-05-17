import requests
import datetime

api_key = '7e4e1a728953773c127b7d60315494a4'
app_id = '5cfa754f'

# Nutritionix API endpoint and headers
nutritionix_api_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': app_id,
    'x-app-key': api_key,
    'Content-Type': 'application/json'
}

# Parameters for the exercise query
exercise_query = {
    'query': 'i ran for 1 mile'
}

# Sending a POST request to the Nutritionix API
response = requests.post(url=nutritionix_api_endpoint, json=exercise_query, headers=headers)
exercise_data = response.json()

# Sheety API endpoint
sheety_api_endpoint = 'https://api.sheety.co/8887817d3c2771a9c71be1314eb79cc9/copyOfMyWorkouts/workouts'

# Constructing the data to be sent to Sheety API
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

sheety_data = {
    'workout': {
        'date': now,
        'time': now,
        'exercise': exercise_data['exercises'][0]['name'],
        'duration': exercise_data['exercises'][0]['duration_min'],
        'calories': exercise_data['exercises'][0]['nf_calories']
    }
}

# Sending a POST request to the Sheety API with error handling
try:
    response = requests.post(sheety_api_endpoint, json=sheety_data)
    response.raise_for_status()  # Raise an exception for non-2xx responses
    print("Data added successfully.")
except requests.exceptions.RequestException as e:
    print(f"Error adding data: {e}")
