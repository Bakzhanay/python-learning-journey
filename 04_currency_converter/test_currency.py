import pytest
from currency_logic import convert_currency, get_exchange_rate

def test_get_exchange_rate_success():
    # Проверяем, что для реальной валюты возвращается число (float)
    rate = get_exchange_rate("USD", "EUR")
    assert isinstance(rate, float)
    assert rate > 0


def test_get_exchange_rate_invalid_currency():
    # Проверяем, что при несуществующей валюте код падает с ошибкой
    with pytest.raises(ValueError):
        get_exchange_rate("INVALID", "USD")


def test_convert_currency_valid():
    # Проверяем математику конвертации на фиксированном курсе (мокаем или проверяем логику)
    # Здесь можно проверить, что отрицательная сумма вызывает ошибку
    with pytest.raises(ValueError):
        convert_currency(-100, "USD", "KZT")