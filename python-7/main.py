import requests

def get_weather_data(key, url, lat, lng):
    
    response = requests.get(url)

    return response

def convert_celsius_to_fahrenheit(temperature_f):
    if not isinstance(temperature_f, float) and not isinstance(temperature_f, int):
        raise TypeError('TypeError: Temperature is not a number.')

    temperature_c = int((temperature_f - 32) * 5.0 / 9.0)

    return temperature_c

def get_temperature(lat, lng):
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)

    data = get_weather_data(key, url, lat, lng).json()
    temperature = data.get('currently').get('temperature')

    temperature = convert_celsius_to_fahrenheit(temperature)
    return temperature