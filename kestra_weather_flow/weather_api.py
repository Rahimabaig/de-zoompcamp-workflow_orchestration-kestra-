import requests

api_key = "api_key_here"
city = "city_here"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

temperature = data["main"]["temp"]
description = data["weather"][0]["description"]

outputs = {
    "city": city,
    "temperature": temperature,
    "description": description
}

outputs = {
    "city": city,
    "temperature": temperature,
    "description": description
}

print(outputs.values())

