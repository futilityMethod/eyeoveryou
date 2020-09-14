import requests
import app

base = "http://metaweather.com/api/location/"
search = base + "search"
loc_query = "lattlong"


def get_weather(latlong):
    loc_payload = {loc_query: latlong}
    location_response = requests.get(search, params=loc_payload)

    if location_response.status_code != requests.codes.ok:
        app.logger.error("Failed to get location for latlong:")
        app.logger.error("Got response: " + location_response.status_code)
        return None

    weather = requests.get(base + str(location_response.json()[0]['woeid']))
    if weather.status_code != requests.codes.ok:
        app.logger.error("Failed to get weather info.")
        app.logger.error("Got response: " + weather.status_code)
        return None

    return weather.json()['consolidated_weather'][0]


if __name__ == '__main__':
    default_weather = get_weather("36.96,-122.02")
    print(default_weather['weather_state_name'])