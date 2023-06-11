import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from twilio.rest import Client

load_dotenv(dotenv_path=Path('./twilio.env'))
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
api_key = os.getenv('OPENWEATHERMAP_API_KEY')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
own_phone_number = os.getenv('OWN_PHONE_NUMBER')

parameters = {'q':'Barcelona,ES',
              'appid':api_key}
response = requests.get(url='http://api.openweathermap.org/geo/1.0/direct',
                        params=parameters)
response.raise_for_status()
data = response.json()
lat = data[0]['lat']
lon = data[0]['lon']

parameters = {'lat':lat,
              'lon':lon,
              'units':'metric',
              'appid':api_key}
# Not using the One Call option as it required to give too much personal information
# Hourly data is available only for pro memberships, so I'll be using data every 3 hours
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast',
                        params=parameters)
response.raise_for_status()
data = response.json()

client = Client(account_sid, auth_token)

# Course shows for 12 hours, which here will be 4 elements
# IDs lower than 700 represent some adverse weather (rain, snow, etc.)
if any(data['list'][n]['weather'][0]['id'] < 700 for n in range(4)):
    message = client.messages \
                    .create(
                        body="It's going to rain today, better bring an umbrella ☔",
                        from_=twilio_phone_number,
                        to=own_phone_number
                    )
    print(message.sid)
    print(message.status)
