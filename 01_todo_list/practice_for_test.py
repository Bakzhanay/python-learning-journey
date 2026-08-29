# Тестовая версия main TO-DO практика

def add_task_logic(tasks, task_text):
    cleaned_text = task_text.strip()
    if cleaned_text:
        tasks.append(cleaned_text)
        return True
    else:
        return False

def delete_task_logic(tasks, choice_str):
    try:
        choice = int(choice_str)
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice -1)
            return True
        else:
            return False
    except ValueError:
        return False


def show_tasks_ui(tasks):
    if not tasks:
        print("\nEmpty")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task_ui(tasks):
    task_text = input("Write your tasks here: ")
    success = add_task_logic(tasks, task_text)
    if success:
        print("Your task added!")
    else:
        print("Try again")


def delete_task_ui(tasks):
    show_tasks_ui(tasks)
    if not tasks:
        return
    choice_str = input("Write a number which you want to delete: ")
    success = delete_task_logic(tasks, choice_str)
    if success:
        print("Success")
    else:
        print("Try again")


def main():
    tasks = []
    while True:
        print("\nTo-DO LIST")
        print("1. Show all")
        print("2. Add one")
        print("3. Del")
        print("4. Exit")

        choice = input("Choose a number: ").strip()

        if choice == "1":
            show_tasks_ui(tasks)
        elif choice == "2":
            add_task_ui(tasks)
        elif choice == "3":
            delete_task_ui(tasks)
        elif choice == "4":
            print("Bye...")
            break
        else:
            print("Syntax error: Try again")


if __name__ == "__main__":
    main()