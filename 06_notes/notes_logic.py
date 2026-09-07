import json 
from pathlib import Path

# Определяем путь к файлу через pathlib
NOTES_FILE = Path("notes.json")

def load_notes() -> list:
    """Загружает заметки из файла, если он существует"""
    if not NOTES_FILE.exists():
        return []

    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Защита от поврежденного файла (если там пустой или битый JSON)
        return []


def save_notes(notes: list) -> None:
    """Сохраняет список заметок в файл."""
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        # ensure_ascii=False сохраняет кириллицу в читаемом виде, indent=2 делает файл красивым
        json.dump(notes, f, ensure_ascii=False, indent=2)


def add_note(text: str) -> None:
    """Добавлякт новую заметку и сохраняет состояние."""
    notes = load_notes()
    notes.append({"id": len(notes) +1, "text": text})
    save_notes(notes)
    print(f"Заметка сохранена!")


if __name__ == "__main__":
    add_note("Купить продукты")
    print("Текущие заметки:", load_notes())