import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

params = {
    "lat": 19.377713,
    "lng": -99.105526
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print("sunset", sunset)
print("sunrise", sunrise)

