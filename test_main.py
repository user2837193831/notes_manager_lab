from main import (
    add_note,
    find_note,
    add_tag,
    long_notes
)

def test_add_note():
    notes = []
    add_note(notes, "Купить хлеб")
    assert notes == ["Купить хлеб"]
    add_note(notes, "Сдать лабу")
    assert notes == ["Купить хлеб", "Сдать лабу"]

def test_find_note():
    notes = ["Купить хлеб", "Сдать лабу по Python", "Позвонить маме"]
    assert find_note(notes, "мам") == [(2, "Позвонить маме")]
    assert find_note(notes, "Python") == [(1, "Сдать лабу по Python")]
    assert find_note(notes, "кот") == []

def test_add_tag():
    tags = {0: {"работа"}}
    add_tag(tags, 0, "срочно")
    add_tag(tags, 1, "учёба")
    add_tag(tags, 1, "учёба")
    assert tags[0] == {"работа", "срочно"}
    assert tags[1] == {"учёба"}

def test_long_notes():
    notes = ["короткая", "это достаточно длинная заметка", "12 символов "]
    assert long_notes(notes) == ["это достаточно длинная заметка"]
