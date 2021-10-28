import requests
WEATHER_API_URL='http://api.weatherapi.com/v1/current.json'
WEATHER_API_KEY='e9a0950268484d07927114250212310'



def query_api(city):
    try:
        data = requests.get (WEATHER_API_URL + "?key=" + WEATHER_API_KEY + "&q=" + city + "&aqi=yes").json()
    except Exception as exc:
        print(exc)
        data = None
    return data
