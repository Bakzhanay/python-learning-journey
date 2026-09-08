import notes

def show_notes():
    data = notes.load_notes()
    if not data:
        print("\nСписок заметок пуст.")
        return
    print("\n--- Ваши заметки ---")
    for item in data:
        print(f"{item['id']}. {item['text']}")

def handle_add():
    text = input("Введите текст заметки: ").strip()
    if text:
        notes.add_note(text)
        print("Заметка добавлена!")
    else:
        print("Ошибка: заметка не может быть пустой.")

def handle_delete():
    show_notes()
    data = notes.load_notes()
    if not data:
        return
    
    choice_str = input("Введите номер заметки для удаления: ")
    try:
        idx = int(choice_str)
        if notes.delete_note(idx):
            print("Заметка успешно удалена.")
        else:
            print("Ошибка: заметки с таким номером нет.")
    except ValueError:
        print("Ошибка: введите число.")

def main():
    while True:
        print("\n--- Меню ---")
        print("1. Посмотреть все заметки")
        print("2. Добавить заметку")
        print("3. Удалить заметку")
        print("q. Выход")
        
        user_input = input("Выберите действие: ").strip().lower()

        if user_input == "q":
            print("Завершение работы.")
            break
        elif user_input == "1":
            show_notes()
        elif user_input == "2":
            handle_add()
        elif user_input == "3":
            handle_delete()
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()