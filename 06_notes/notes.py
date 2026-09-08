import json
from pathlib import Path

NOTES_FILE = Path("notes.json")

def load_notes() -> list:
    """Загружает заметки из файла."""
    if not NOTES_FILE.exists():
        return []
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_notes(notes: list) -> None:
    """Сохраняет список заметок в файл."""
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

def add_note(text: str) -> None:
    """Создает заметку и сохраняет файл."""
    notes = load_notes()
    notes.append({"id": len(notes) + 1, "text": text})
    save_notes(notes)

def delete_note(index: int) -> bool:
    """Удаляет заметку по порядковому номеру (1-based) и сохраняет изменения."""
    notes = load_notes()
    if 1 <= index <= len(notes):
        notes.pop(index - 1)
        # Пересчитываем ID для порядка
        for i, note in enumerate(notes, start=1):
            note["id"] = i
        save_notes(notes)
        return True
    return False