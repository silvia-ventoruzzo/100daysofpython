import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from twilio.rest import Client

load_dotenv(dotenv_path=Path('./twilio.env'))
ALPHAVANTAGE_API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
NEWSAPI_API_KEY = os.getenv('NEWSAPI_API_KEY')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
own_phone_number = os.getenv('OWN_PHONE_NUMBER')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {'function':'TIME_SERIES_DAILY_ADJUSTED',
              'symbol':STOCK,
              'interval':'60min',
              'apikey':ALPHAVANTAGE_API_KEY}
response = requests.get(url='https://www.alphavantage.co/query',
                        params=parameters)
response.raise_for_status()
stock_data = response.json()
daily_data = stock_data['Time Series (Daily)']
last_two_closes = [daily_data[day]['4. close'] for day in list(daily_data.keys())[:2]]
stock_change = float(last_two_closes[0])/float(last_two_closes[1]) - 1
abs_stock_change = abs(stock_change)

if abs_stock_change >= 0.05:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    parameters = {'apiKey':NEWSAPI_API_KEY,
                  'q':COMPANY_NAME}
    response = requests.get(url='https://newsapi.org/v2/everything',
                            params=parameters)
    response.raise_for_status()
    news_data = response.json()
    top_news = [news_data['articles'][n] for n in range(3)]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 
    client = Client(account_sid, auth_token)

    arrow = '🔺' if stock_change > 0 else '🔻'
    abs_stock_change = int(abs_stock_change*100)

    for news in top_news:
        message_text = f"{STOCK}: {arrow}{abs_stock_change}%\nHeadline: {news['title']}\nBrief: {news['description']}"
        message = client.messages \
                        .create(
                            body=message_text,
                            from_=twilio_phone_number,
                            to=own_phone_number
                        )
        print(message.sid)
        print(message.status)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

