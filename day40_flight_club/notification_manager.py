from twilio.rest import Client
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

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
        
    def send_emails(self, message):
        pass 
        # not possible as it was not working for my email provider
