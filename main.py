import requests

api_key = "6311bdd8055d12e9d877464f3c124e12"

# Took the url from open whether api
url = "https://api.openweathermap.org/data/2.5/weather?units=metric&"

# Took the input from the user
city_name = input("Enter city name: ")

# Created final url with addition of api_key and city_name
Final_url = url + "appid=" + api_key + "&q=" + city_name

response = requests.get(Final_url).json()

temperature = response['main']['temp']

print(temperature)