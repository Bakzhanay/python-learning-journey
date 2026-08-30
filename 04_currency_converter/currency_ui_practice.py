from currency_logic_practice import get_exchange_rate, convert_currency

def main():
    print("Конвертер валют")

    try:
        base = input("Введите первое значение (например: USD, KZT, EUR): ").strip()
        target = input("Введите второе значение (например: EUR, USD, RUB): ").strip()
        amount_str = input(f"Введите сумму для конвертации ({base.upper()}): ").strip()

        amount = float(amount_str)

        rate = get_exchange_rate(base, target)
        result = convert_currency(amount, base, target)

        print(f"\nТекущий курс: {base.upper()} = {rate} {target.upper()}")
        print(f"\nРезультат: {amount} {base.upper()} = {result} {target.upper()}")

    except ValueError as e:
        print(f"\n[Ошибка ввода]: {e}")
    except ConnectionError as e:
        print(f"\n[Ошибка сети]: {e}")
    except Exception as e:
        print(f"\n[Непридведенная ошибка]: {e}")


if __name__ == "__main__":
    main()