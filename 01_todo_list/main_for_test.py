# --- ЧИСТАЯ БИЗНЕС-ЛОГИКА (её мы и будем тестировать) ---

def add_task_logic(tasks, task_text):
    """Добавляет задачу, если она не пустая. Возвращает True/False."""
    cleaned_text = task_text.strip()
    if cleaned_text:
        tasks.append(cleaned_text)
        return True
    return False


def delete_task_logic(tasks, choice_str):
    """Удаляет задачу по строковому индексу от пользователя. Возвращает True/False."""
    try:
        choice = int(choice_str)
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice -1)
            return True
        return False
    except ValueError:
        return False


# --- Интерфейсная часть (ввод/вывод) ---

def show_tasks(tasks):
    if not tasks:
        print("\nПустое значение.")
        return
    
    print("\nВаши задачи:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task_ui(tasks):
    task_text = input("Напишите вашу задачу: ").strip()
    success = add_task_logic(tasks, task_text)
    if success:
        print("Задача успешно выполнена")
    else:
        print("Неправильное значение. Повторите попытку.")


def delete_task_ui(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    
    choice_str = input("Выберите нумерацию задачи которую хотите удалить: ")
    success = delete_task_logic(tasks, choice_str)
    if success:
        print("Задача удалена.")
    else:
        print("Ошибка: неверный номер.")


def main():
    tasks = []
    while True:
        print("\n TO DO LIST ")
        print("1. Show all")
        print("2. Add")
        print("3. Del")
        print("4. Exit")

        choice = input("Choose one: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task_ui(tasks)
        elif choice == "3":
            delete_task_ui(tasks)
        elif choice == "4":
            print("See you later...")
            break
        else:
            print("Ошибка: Выберите цифру от 1 до 4.")


if __name__=="__main__":
    main()
            