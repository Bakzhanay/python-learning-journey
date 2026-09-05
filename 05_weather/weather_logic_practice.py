import requests

def get_weather(lat: str, lon:str) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	    "latitude": lat,
	    "longitude": lon,
	    "current_weather": True,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "current_weather" in data:
            return data["current_weather"]

        raise ValueError("Ошибка с получением погоды.")

    except requests.RequestException as e:
        raise ConnectionError(f"Ошибка подключения к сети погоды: {e}")


def get_coordinates(city_name: str) -> tuple[float, float]:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name,
        "count": 1,
        "language": "ru",
        "format": "json"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if "results" in data and len(data["results"]):
        location = data["results"][0]
        return location["latitude"], location["longitude"]

    raise ValueError(f"Город {city_name} не найден.")


def get_weather_description(code: int) -> str:
    mapping = {
        00: "Облачность уменьшается.",
        1: "Облака рассеиваются.",
        2: "Состояние неба без изменений.",
        3: "Облачность увеличивается.",
        61: "Слабый дождь.",
        71: "Слабый снег."
    }
    return mapping.get(code, f"Код погоды: {code}")