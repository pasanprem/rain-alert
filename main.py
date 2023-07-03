api_key = "69f04e4613056b159c2761a9d9e664d2"

import requests

# parameters = {
#     "lat":51.5085,
#     "lon":-0.1257,
#     "appid":api_key,
#     "exclude":"current,minutely,daily"
# }

parameters = {
    "lat":33.573109,
    "lon":--7.589843,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)

# print(weather_data["hourly"][0]["weather"][0]["id"])

count = 0
raining = 0
while count < 12:
    if weather_data["hourly"][count]["weather"][0]["id"] < 700:
        raining = 1
    count += 1

if raining == 1:
    print("Bring your umbrella")
else:
    print("It is not going to rain!")