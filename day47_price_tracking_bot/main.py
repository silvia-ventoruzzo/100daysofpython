import os
from dotenv import load_dotenv
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
import requests
from twilio.rest import Client

# I'll be sending SMS instead of email as email connection was not working
load_dotenv(dotenv_path=Path('./twilio.env'))
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
OWN_PHONE_NUMBER = os.getenv('OWN_PHONE_NUMBER')

# Get price from website
url = 'https://www.amazon.es/AmazonBasics-Barra-tensi%C3%B3n-Cortina-N%C3%ADquel/dp/B073Q73B9H/ref=pd_ybh_a_sccl_8/262-1660601-8696564?pd_rd_w=cW4aC&content-id=amzn1.sym.58609157-3ccd-44a9-9919-6f49add6e0e5&pf_rd_p=58609157-3ccd-44a9-9919-6f49add6e0e5&pf_rd_r=6BG5RQYPRFQFRCAC83ET&pd_rd_wg=31Jhz&pd_rd_r=ea39d134-ab2b-4651-a434-c8b14664d881&pd_rd_i=B073Q73B9H&psc=1'
headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'Accept-Language':'it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name="span", class_="a-offscreen").get_text()
price = float(price.replace(',', '.').replace('€', ''))

if price is None:
    print('Price not found')
    exit()

# Send SMS if price below desired level
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

if price < 20:
    message = client.messages \
                    .create(
                        body="The kitchen bar is finally below 20€, go buy it!",
                        from_=TWILIO_PHONE_NUMBER,
                        to=OWN_PHONE_NUMBER
                    )
    print(message.sid)
    print(message.status)