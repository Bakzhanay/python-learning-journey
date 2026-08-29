from password_practice_logic import generate_password

def main():
    print("---ГЕНЕРАТОР ПАРОЛЕЙ---")

    while True:
        try:
            length = int(input("Напишите длину вашего пароля (минимум 4): "))
            if length <4 or length >50:
                print("Длина не должна быть меньше 4 или выше 50.")
                continue
            break
        except ValueError:
            print("Ошибка: Повторите попытку")

    choice = input("Хотите ли вы чтобы в пароле присутствовали символы? (д/н).").strip().upper()
    use_symbols = choice != "н"

    try:
        password = generate_password(length, use_symbols)
        print(f"Ваш пароль: {password}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()