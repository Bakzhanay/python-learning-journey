from unittest.mock import patch
import requests 
import pytest
from weather_logic_practice import get_weather, get_coordinates, get_weather_description

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        pass


def test_get_weather_success():
    fake_data = {
        "current_weather": {
            "temperature": 20.5,
            "windspeed": 5.0,
            "weather_code": 0
        }
    }

    with patch("weather_logic_practice.requests.get", return_value=MockResponse(fake_data)):
        result = get_weather(51.18, 71.45)

        assert result["temperature"] == 20.5
        assert result["weather_code"] == 0


def test_get_weather__connection_error():
    with patch("weather_logic_practice.requests.get", side_effect=requests.RequestException):
        with pytest.raises(ConnectionError):
            get_weather(51.18, 71.45)


def test_get_weather_descpription_known():
    assert get_weather_description(0) == "Облачность уменьшается."
    assert get_weather_description(61) == "Слабый дождь."


def test_get_weather_descpription_unknown():
    assert get_weather_description(999) == "Код погоды: 999"

def test_get_coordinates():
    fake_data = {
        "results": [
            {
                "latitude": 51.18,
                "longitude": 71.45
            }
        ]
    }
    with patch("weather_logic.requests.get", return_value=MockResponse(fake_data)):
        lat, lon = get_coordinates("Астана")
        assert isinstance(lat, float)
        assert isinstance(lon, float)
        assert lat == 51.18
        assert lon == 71.45