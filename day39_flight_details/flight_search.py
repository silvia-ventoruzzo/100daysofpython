import requests
import os
from dotenv import load_dotenv
from pathlib import Path

from day39_flight_details.flight_data import FlightData

load_dotenv(dotenv_path=Path('./twilio.env'))
KIWI_API_KEY = os.getenv('KIWI_API_KEY')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        self.endpoint =  'https://tequila-api.kiwi.com'
        self.headers = {
            "apikey": KIWI_API_KEY
        }
    
    def find_iata_code(self, city_name):
        location_endpoint = f"{self.endpoint}/locations/query"
        params = {
            "term": city_name, 
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=self.headers, params=params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    
    def get_cheap_flights(self, **kwargs):
        search_endpoint = f"{self.endpoint}/v2/search"
        response = requests.get(url=search_endpoint, headers=self.headers, params=kwargs)
        response.raise_for_status()
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {kwargs.get('fly_to')}.")
            return None

        fly_from_iata = data['flyFrom']
        fly_from_city = data['cityFrom']
        fly_to_iata = data['flyTo']
        fly_to_city = data['cityTo']
        price = data['price']
        out_airline = data['route'][0]['airline']
        out_time = data['route'][0]['local_departure']
        return_airline = data['route'][1]['airline']
        return_time = data['route'][1]['local_departure']
        
        flight_data = FlightData(fly_from_iata=fly_from_iata,
                                 fly_from_city=fly_from_city,
                                 fly_to_iata=fly_to_iata,
                                 fly_to_city=fly_to_city,
                                 price=price,
                                 out_airline=out_airline,
                                 out_time=out_time,
                                 return_airline=return_airline,
                                 return_time=return_time)
        return flight_data