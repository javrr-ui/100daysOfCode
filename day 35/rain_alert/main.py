import requests
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()

url = f"https://api.openweathermap.org/data/3.0/onecall?lat={19.432608}&lon={-99.133209}&appid={os.getenv("API_KEY")}"
response = requests.get(url)
print(f"Status code: {response.status_code}")
print(response.json())
