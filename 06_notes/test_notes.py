import pytest
import notes
from notes import add_note, delete_note

def test_add_note_example(tmp_path, monkeypatch):
    # 1. Создаем временный путь
    test_file = tmp_path / "test_notes.json"
    
    # 2. Подменяем NOTES_FILE в модуле notes на временный файл
    monkeypatch.setattr(notes, "NOTES_FILE", test_file)

    # 3. Выполняем тестируемое действие
    notes.add_note("Тестовая запись")

    # 4. Проверяем результат через assert
    result = notes.load_notes()
    assert len(result) == 1
    assert result[0]["text"] == "Тестовая запись"

def test_delete_note_success(tmp_path, monkeypatch):
    # 1. ПОДГОТОВКА (Setup)
    # Создаем временный файл и подменяем константу в notes.py
    test_file = tmp_path / "test_notes.json"
    monkeypatch.setattr(notes, "NOTES_FILE", test_file)

    # Создаем 2 заметки в файле (они получат id 1 и 2)
    notes.add_note("Первая заметка")
    notes.add_note("Вторая заметка")

    # 2. ДЕЙСТВИЕ (Action)
    # Удаляем первую заметку (индекс 1)
    result = notes.delete_note(1)

    # 3. ПРОВЕРКА (Assert)
    # Проверяем, что функция вернула True
    assert result is True

    # Считываем актуальные данные из файла и проверяем остаток
    remaining_notes = notes.load_notes()
    assert len(remaining_notes) == 1
    assert remaining_notes[0]["text"] == "Вторая заметка"

def test_delete_note_invalid_index(tmp_path, monkeypatch):
    # 1. ПОДГОТОВКА
    test_file = tmp_path / "test_notes.json"
    monkeypatch.setattr(notes, "NOTES_FILE", test_file)

    # Создаем 1 заметку
    notes.add_note("Единственная заметка")

    # 2. ДЕЙСТВИЕ
    # Пытаемся удалить несуществующий номер 99
    result = notes.delete_note(99)

    # 3. ПРОВЕРКА
    # Функция должна вернуть False
    assert result is False

    # Количество заметок в файле не должно измениться
    remaining_notes = notes.load_notes()
    assert len(remaining_notes) == 1