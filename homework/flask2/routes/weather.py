from flask import request, render_template, Response
from app import app
from config import Config
import requests


@app.route('/weather', methods=['POST'])
def weather():
        weather = []
        cities = request.form.get("cities")
        cities = cities.replace(" ", "")
        cities_list = cities.split(",")
        for city in cities_list:
            querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                           "units": "metric"}
        response = requests.get(Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + cities_list + "&aqi=yes"
        )
        return response.json()

@app.route('/get-your-weather')
def yourWeather():
    return render_template('weather.html')
