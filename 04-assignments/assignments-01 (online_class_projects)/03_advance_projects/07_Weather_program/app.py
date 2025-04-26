# Importing pprint for better formatted output of JSON data
from pprint import pprint

# Importing requests module to make HTTP requests
import requests

# Importing load_dotenv and os for loading environment variables from .env file
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the WEATHER_API_KEY stored in the .env file
API_KEY = os.getenv("WEATHER_API_KEY")

# Asking user to input the city name
city = input("Enter the city: ")

# Creating the API URL with the entered city and the API key
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# Sending a GET request to the weather API and storing the JSON response
weather_data = requests.get(base_url).json()

# Nicely printing the JSON weather data
pprint(weather_data)