import requests

def get_exchange_rate(base_currency: str, target_currency:str) -> float:
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("result") == "success":
            rates = data.get("rates", {})
            if target_currency.upper() in rates:
                return float(rates[target_currency.upper()])
            
            raise ValueError("Целевая валюта не найдена. Попробуйте еще раз")

        if data.get("result") != "success":
            raise ValueError("Некорректный код базовой валюты")

    except requests.RequestException as e:
        raise ConnectionError("Ошибка подключения к сети")


def convert_currency(amount: float, base_currency: str, target_currency: str) -> float:
    if amount < 0:
        raise ValueError("Значение не может быть отрицательным")

    rate = get_exchange_rate(base_currency, target_currency)
    return round(amount * rate, 2)
