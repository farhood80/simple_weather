import requests
import json

API_key = "2b38b7387c54998568952b8fa6244fd4"
city_name = input("please enter the location: ")
URL =f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

res = requests.get(URL)
json_data = json.loads(res.next)
weather = json_data["weather"][0]["description"]
temprature = json_data["main"]["temp"] 
humidity = json_data["main"]["humidity"]
wind_speed = json_data["wind"]["speed"]

print(f"Weather: {weather}")
print(f"Temprature: {temprature}")
print(f"Humidity: {humidity}")
print(f"Wind speed: {wind_speed}")