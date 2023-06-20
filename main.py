api_key = "69f04e4613056b159c2761a9d9e664d2"

import requests

parameters = {
    "lat":51.5085,
    "lon":-0.1257,
    "appid":api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
data = response.json()

print(data)