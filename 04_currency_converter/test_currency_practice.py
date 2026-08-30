import pytest
from currency_logic_practice import get_exchange_rate, convert_currency

def test_get_exchange_rate_success():
    rate = get_exchange_rate("USD", "EUR")
    assert isinstance(rate, float)
    assert rate > 0


def test_get_exchange_rate_invalid_currency():
    with pytest.raises(ValueError):
        get_exchange_rate("INVALID", "USD")


def test_convert_currency_valid():
    with pytest.raises(ValueError):
        convert_currency(-100,"USD", "RUB")