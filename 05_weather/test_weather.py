from unittest.mock import patch
import pytest
import requests
from weather_logic import get_weather_description, get_weather, get_coordinates

# Создаем класс-заглушку для ответа requests
class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        pass # Ничего не делает, значит, ошибки HTTP нет

def test_get_weather_success():
    # Данные, которые якобы вернул сервер Open-Meteo
    fake_data = {
        "current_weather": {
            "temperature": 20.5,
            "windspeed": 5.0,
            "weathercode": 0
        }
    }

    # Подменяем requests.get так, чтобы он возвращал наш MockResponse
    with patch("weather_logic.requests.get", return_value=MockResponse(fake_data)):
        result = get_weather(51.18, 71.45)

        # Проверяем, что функция вернула именно то, что мы ожидали
        assert result["temperature"] == 20.5
        assert result["weathercode"] == 0

def test_weather_decription_known():
    assert get_weather_description(0) == "Ясное небо"
    assert get_weather_description(61) == "Небольшой дождь"

def test_weather_description_unknown():
    assert get_weather_description(999) == "Код погоды: 999"

def test_get_weather_connection_error():
    # Подменяем requests.get так, чтобы он всегда выбрасывал ошибку сети
    with patch("weather_logic.requests.get", side_effect=requests.RequestException):
        with pytest.raises(ConnectionError):
            get_weather(51.18, 71.45)

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
