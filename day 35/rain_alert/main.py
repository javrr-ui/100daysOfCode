import requests

api_key = "6305e293bf13b8ae394e4574bf17e79d"
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={19.432608}&lon={-99.133209}&appid={api_key}"
response = requests.get(url)
print(f"Status code: {response.status_code}")
print(response.json())
