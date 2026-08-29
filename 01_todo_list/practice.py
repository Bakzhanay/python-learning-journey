# TO-DO LIST little project practice

def show_tasks(tasks):
    if not tasks:
        print("\nПусто")
        return
    print("\nВаши задачи: ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    task = input("Введите вашу задачу: ").strip()
    if task:
        tasks.append(task)
        print(f"Ваша задача добавлена '{task}'.")
    else:
        print("Ошибка: Повторите попытку (возможно некорректное значение).")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Выберите цифру какую задачу хотите удалить: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice -1)
            print(f"Ваша задача: '{removed}' - удалена.")
        else:
            print("Ошибка: Некорректное значение, попробуйте еще")
    except ValueError:
        print("Ошибка: Некорректное значение, попробуйте еще")


def main():
    tasks = []
    while True:
        print("\n---TO-DO LIST---")
        print("1. Показать всё")
        print("2. Добавить")
        print("3. Удалить")
        print("4. Выйти")

        choice = input("Выберите из списка значение: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Вы выходите...")
            break
        else:
            print("Ошибка: Некорректное значение")


if __name__ == "__main__":
    main()