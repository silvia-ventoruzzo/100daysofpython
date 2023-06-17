import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from twilio.rest import Client

load_dotenv(dotenv_path=Path('./twilio.env'))
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
OWN_PHONE_NUMBER = os.getenv('OWN_PHONE_NUMBER')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self):
        pass
    
    def send_notification(self,
                          fly_from_iata, fly_from_city,
                          fly_to_iata, fly_to_city,
                          price, out_date, return_date):
        
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message_text = f"Low price alert! Only {price}€ to fly from {fly_from_city}-{fly_from_iata} to {fly_to_city}-{fly_to_iata} from {out_date} to {return_date}"
        message = client.messages \
                        .create(
                            body=message_text,
                            from_=TWILIO_PHONE_NUMBER,
                            to=OWN_PHONE_NUMBER
                        )
        print(message.sid)
        print(message.status)