from main_for_test import add_task_logic, delete_task_logic

def test_add_task_success():
    tasks = []
    result = add_task_logic(tasks, "  Купить молоко  ")

    assert result is True
    assert tasks == ["Купить молоко"] # `.strip()` должен сработать

def test_add_task_empty():
    tasks = []
    result = add_task_logic(tasks, "    ")

    assert result is False
    assert tasks == []

def test_delete_task_success():
    tasks = ["Задача 1", "Задача 2"]
    result = delete_task_logic(tasks, "1")

    assert result is True
    assert tasks == ["Задача 2"] # рамки сдвинулись

def test_delete_task_invalid_number():
    tasks = ["Задача 1"]
    result = delete_task_logic(tasks, "5") # такого номера нет

    assert result is False
    assert len(tasks) == 1

def test_delete_task_not_a_number():
    tasks = ["Задача 1"]
    result = delete_task_logic(tasks, "abc") # буквы вместо цифры

    assert result is False
    assert len(tasks) == 1