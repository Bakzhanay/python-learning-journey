from currency_logic import convert_currency, get_exchange_rate

def main():
    print("=== Конвертер валют ===")

    try:
        base = input("Введите исходную валюту (например: USD, KZT, EUR): ").strip()
        target = input("Введите целевую валюту (например: EUR, USD, RUB): ").strip()
        amount_str = input(f"Введите сумму для конвертации ({base.upper()}): ").strip()

        amount = float(amount_str) 

        rate = get_exchange_rate(base, target)
        result = convert_currency(amount, base, target)

        print(f"\nТекущий курс: {base.upper()} = {rate} {target.upper()}")
        print(f"Результат: {amount} {base.upper()} = {result} {target.upper()}")

    except ValueError as e:
        print(f"\n[Ошибка ввода]: {e}")
    except ConnectionError as e:
        print(f"\n[Ошибка сети]: {e}")
    except Exception as e:
        print(f"\n[Непредвиденная ошибка]: {e}")


if __name__ == "__main__":
    main()