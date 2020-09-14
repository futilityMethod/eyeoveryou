import requests

base = "http://metaweather.com/api/location/"
search = base + "search"
loc_query = "lattlong"

def get_weather(latlong):
    loc_payload = {loc_query: latlong}
    location_response = requests.get(search, params=loc_payload).json()
    weather = requests.get(base + str(location_response[0]['woeid'])).json()
    return weather['consolidated_weather'][0]


if __name__ == '__main__':
    weather = get_weather("36.96,-122.02")
    print(weather['weather_state_name'])