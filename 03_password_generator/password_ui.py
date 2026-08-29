from password_logic import generate_password

def main():
    print("ГЕНЕРАТОР ПАРОЛЕЙ")

    while True:
        try:
            length = int(input("Введите длину пароля (минимум 4): "))
            if length <4 or length > 50:
                print("Ошибка: длина должна быть от 4 до 50 символов.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число.")

    # Выбор спецсимволов
    choice = input("Использовать спецсимволы? (y/n): ").strip().lower()
    use_symbols = choice != 'n'

    try:
        password = generate_password(length, use_symbols)
        print(f"\nСгенерированный пароль: {password}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()