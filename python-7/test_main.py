from main import get_temperature, get_weather_data, convert_celsius_to_fahrenheit
import pytest 

@pytest.mark.parametrize('temperature', [62, 80, 40])
def test_convert_celsius_to_fahrenheit_expected_inputs(temperature):
    temperature_c = convert_celsius_to_fahrenheit(temperature)

    assert temperature_c ==  int((temperature - 32) * 5.0 / 9.0)

@pytest.mark.parametrize('temperature', ['a', None])
def test_convert_celsius_to_fahrenheit_wrong_type_inputs(temperature):
    with pytest.raises(TypeError):
        convert_celsius_to_fahrenheit(temperature)

def test_get_weather_data_correct_url():
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    lat = -14.235004
    lng = -51.92528
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)

    response = get_weather_data(key, url, lat, lng)

    assert response.status_code == 200

def test_get_weather_data_url_not_found():
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    lat = -14.235004
    lng = -51.92528
    url = 'http://httpbin.org/status/404'

    response = get_weather_data(key, url, lat, lng)

    assert response.status_code == 404

