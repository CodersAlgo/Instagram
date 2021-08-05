import requests, json
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Enter your city name here to know its wheather"
API_KEY = "Enter your api key here from open wheather map"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"
response = requests.get(URL)

if response.status_code == 200:
   data = response.json()
   main = data['main']
   temperature = main['temp']
   temp_feel_like = main['feels_like']
   humidity = main['humidity']
   pressure = main['pressure']
   weather_report = data['weather']
   wind_report = data['wind']

   print(f"\n{CITY:-^35}  ")
   print(f"City ID: {data['id']}")
   print(f"Temperature: {temperature}")
   print(f"Feel Like: {temp_feel_like}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {weather_report[0]['description']}")
   print(f"Wind Speed: {wind_report['speed']}")
   print(f"Time Zone: {data['timezone']}\n")
else:
   print("Error in the HTTP request")
