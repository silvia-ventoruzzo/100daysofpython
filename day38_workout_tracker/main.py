import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

load_dotenv(dotenv_path=Path('./twilio.env'))
NUTRITIONIX_API_ID = os.getenv('NUTRITIONIX_API_ID')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
SHEETY_EXERCISE_AUTH = os.getenv('SHEETY_EXERCISE_AUTH')

# Set up exercise information extraction
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id':NUTRITIONIX_API_ID,
    'x-app-key':NUTRITIONIX_API_KEY,
    'Content-Type': 'application/json'
}
exercise_params = {
    'query':'did reformer pilates for 50 minutes'
}
exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
exercise_info = exercise_response.json()

current_timestamp = datetime.now()
date = current_timestamp.strftime('%d/%m/%Y')
time = current_timestamp.strftime('%H:%M:%S')

for ex in exercise_info['exercises']:
    exercise = ex['name']
    duration = ex['duration_min']
    calories = ex['nf_calories']

    # Put information into Google Sheet
    sheety_endpoint = 'https://api.sheety.co/1104efb497ebdc4f2c7dbfe07df44cd5/workoutTracking/workouts'
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            'exercise': exercise.title(),
            'duration': duration,
            'calories': calories
        }
    } 
    headers = {
        'Authorization': f'Basic {SHEETY_EXERCISE_AUTH}'
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers)
