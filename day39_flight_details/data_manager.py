import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
import numpy as np

load_dotenv(dotenv_path=Path('./twilio.env'))
SHEETY_FLIGHT_AUTH = os.getenv('SHEETY_FLIGHT_AUTH')

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.endpoint = 'https://api.sheety.co/1104efb497ebdc4f2c7dbfe07df44cd5/flightDeals/prices' 
        self.headers = {
            'Authorization': f'Basic {SHEETY_FLIGHT_AUTH}'
        }
    
    def get_data(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()
        flight_data = pd.DataFrame(response.json()['prices'])
        flight_data = flight_data.apply(lambda x: x.replace('', np.nan))
        return flight_data
    
    def add_iata_code(self, iata_codes):
        for n in iata_codes.index:
            params = {
                "price": {
                    "iataCode": iata_codes[n]
                }
            }
            response = requests.put(
                url=f"{self.endpoint}/{n+2}",
                json=params,
                headers=self.headers
            )
            response.raise_for_status()