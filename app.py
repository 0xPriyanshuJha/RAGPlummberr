import requests
import os
import dotenv


dotenv.load_dotenv()


api_key = os.getenv("API_KEY")
your_query = "What is Machine Learning"


header = {
    'Content-type': 'application/json',
    'Apikey': api_key,
}


data = {
    "payload": your_query
}

channel_token = "Your Channel Token"
endpoint_id = "Your Endpoint ID" 
url = f'https://payload.vextapp.com/hook/{endpoint_id}/catch/{channel_token}'

response = requests.post(url, headers=header, json=data)

print(response.text)
