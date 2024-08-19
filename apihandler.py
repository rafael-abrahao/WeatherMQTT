import requests

api_key= "38589300af199db56c0b4061f6ef7757"

def get_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid='+ api_key
    response = requests.get(url)
    return response.json()