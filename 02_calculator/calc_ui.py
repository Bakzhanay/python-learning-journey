from calc_logic import add, subtract, multiply, divide

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введено не число. Попробуй еще раз.")

def main():
    while True:
        print("\nКалькулятор")
        print("1. Сложить (+)")
        print("2. Вычесть (-)")
        print("3. Умножить (*)")
        print("4. Разделить (/)")
        print("5. Выход.")

        choice = input("Выбери пункт: ").strip()

        if choice == "5":
            break

        if choice in ("1", "2", "3", "4"):
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")

            try:
                if choice == "1":
                    print(f"Результат: {add(a, b)}")
                elif choice == "2":
                    print(f"Результат {subtract(a, b)}")
                elif choice == "3":
                    print(f"Результат {multiply(a, b)}")
                elif choice == "4":
                    print(f"Результат: {divide(a, b)}")
            except ZeroDivisionError as e:
                print(f"Ошибка: {e}")
        else:
            print("Неверный выбор. Введите цифру от 1 до 5.")


if __name__== "__main__":
    main()