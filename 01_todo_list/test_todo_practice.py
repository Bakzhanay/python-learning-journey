from practice_for_test import add_task_logic, delete_task_logic, show_tasks_ui

def test_add_task_strip():
    tasks = []
    result = add_task_logic(tasks, "    Купить молоко   ")

    assert result is True
    assert tasks == ["Купить молоко"]

def test_add_task_empty():
    tasks = []
    result = add_task_logic(tasks, "    ")

    assert result is False
    assert tasks == []

def test_delete_task_check():
    tasks = ["Task 1", "Task 2"]
    result = delete_task_logic(tasks, "1")

    assert result is True
    assert tasks == ["Task 2"]

def test_delete_task_ivalid_number():
    tasks = ["Task 1"]
    result = delete_task_logic(tasks, "5")

    assert result is False
    assert len(tasks) == 1

def test_delete_task_not_a_number():
    tasks = ["Task 1"]
    result = delete_task_logic(tasks, "abc")

    assert result is False
    assert len(tasks) == 1

def test_show_tasks_ui_empty(capsys):
    tasks = []
    show_tasks_ui(tasks)

    # capsys - это встроенный инструмент pytest, который ловит то, что летит в print
    captured = capsys.readouterr()
    assert "Empty" in captured.out # Проверяем, что вывелось наше сообщение о пустоте
    assert tasks == []