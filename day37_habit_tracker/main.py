import requests
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv(dotenv_path=Path('./twilio.env'))
PIXELA_TOKEN = os.getenv('PIXELA_TOKEN')
PIXELA_USERNAME = 'silviav'
PIXELA_GRAPH = 'graph1'

# https://pixe.la/

# 1. Create your user account
endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token':PIXELA_TOKEN,
    'username':PIXELA_USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}
user_response = requests.post(url=endpoint, json=user_params)
print(user_response.text)

# 2. Create a graph definition
graph_endpoint = f'{endpoint}/{PIXELA_USERNAME}/graphs'
graph_params = {
    'id':PIXELA_GRAPH,
    'name':'coding',
    'unit':'minute',
    'type':'int',
    'color':'ajisai',
    'timezone':'Europe/Madrid'
}
headers = {
    'X-USER-TOKEN':PIXELA_TOKEN
}
graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(graph_response.text)

# 3. Get the graph!
graph_url = f'{graph_endpoint}/{PIXELA_GRAPH}'

# 4. Post value to the graph
today = date.today().strftime('%Y%m%d')
value_params = {
    'date':today,
    'quantity':'60'
}
value_response = requests.post(url=graph_url, json=value_params, headers=headers)
print(value_response.text)
