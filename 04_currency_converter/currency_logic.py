import requests

def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """Запрашивает актуальный курс валют через публичный API."""
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Вызовет ошибку, если статус не 200 (например 404)
        data = response.json()

        if data.get("result") == "success":
            rates = data.get("rates", {})
            if target_currency.upper() in rates:
                return float(rates[target_currency.upper()])

            raise ValueError("Целевая валюта не найдена в ответе API.")

        if data.get("result") != "success":
            raise ValueError("Некорректный код базовой валюты.")

    except requests.RequestException as e:
        raise ConnectionError(f"Ошибка сети при запросе к API: {e}")


def convert_currency(amount: float, base_currency: str, target_currency: str) -> float:
    """Конвертирует сумму из одной валюты в другую."""
    if amount <0:
        raise ValueError("Сумма для конвертации не может быть отрицательеой.")

    rate = get_exchange_rate(base_currency, target_currency)
    return round(amount * rate, 2)