import requests
def get_temperature(city):
    response=requests.get(f"http://api.weather.com/{city}")
    data=response.json()
    return data["temperature"]