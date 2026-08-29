def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст.")
        return
    print("\nВаши задачи: ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    task = input("Введите текст задачи: ").strip()
    if task: 
        tasks.append(task)
        print(f"Задача '{task}' добавлена.")
    else: 
        print("Ошибка: задача не может быть пустой.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Введите номер задачи для удаления: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice -1)
            print(f"Удалена задача: '{removed}'")
        else:
            print("Ошибка: Такого номера нет в списке.")
    except ValueError:
        print("Ошибка: Нужно ввести число.")


def main():
    tasks = []
    while True:
        print("\n--TO-DO LIST ---")
        print("1. Посмотреть задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: неверный выбор, введите цифру от 1 до 4.")


if __name__ == "__main__":
    main()