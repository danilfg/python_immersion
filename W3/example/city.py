import pprint
import requests

class OpenWeatherMapForecast:


    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a74d22e67de29ade618db61ec482cdcd&units=metric"
        print("sending HTTP request")
        data = requests.get(url).json()
        forecast_data = data["main"]
        forecast = {}
        forecast["feels_like"] = forecast_data["feels_like"]
        forecast["high_temp"] = forecast_data["temp_max"]
        self._city_cache[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeatherMapForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    weather_forecast = OpenWeatherMapForecast()
    for i  in range(5):
        city_info = CityInfo("Moscow", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()

if __name__ == "__main__":
    _main()