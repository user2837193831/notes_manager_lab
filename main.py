import random
import notes_data

def show_help():
    print("add текст - добавить заметку")
    print("find слово - найти текст в заметках")
    print("list - показать все заметки с тегами")
    print("tag номер тег - добавить тег к заметке")
    print("tags - показать множество всех тегов")
    print("long - показать длинные заметки")
    print("short - показать котроткие заметки")
    print("upper - показать заметки заглавными буквами")
    print("lower - показать заметки строчными буквами")
    print("clear - удалить все заметки и теги")
    print("tip - получить случайную подсказку")
    print("exit - завершить программу")

def add_note(notes, text):
    notes.append(text)

def find_note(notes, word):
    word = word.lower()
    found = []
    for i in range(len(notes)):
        if word in notes[i].lower():
            found.append((i, notes[i]))
    return found

# Добавляет тег(tag) к заметке номер idx; tags = {0: {"дом"}, 1: {"работа"}}
def add_tag(tags, idx, tag):
    if idx not in tags:
        tags[idx] = set()
    tags[idx].add(tag)

# Возвращает множество всех тегов
def get_all_tags(tags):
    all_tags = set()
    for tag_set in tags.values():
        all_tags |= tag_set
    return all_tags

def list_notes(notes, tags):
    if not notes:
        print("Список заметок пуст")
        return
    
    for idx in range(len(notes)):
        line = f"{idx + 1}: {notes[idx]}"
        if idx in tags:
            tag_text = ", ".join(sorted(tags[idx]))
            line = f"{line} [{tag_text}]"
        print(line)

def print_list(items):
    if not items:
        print("Ничего нет")
    else:
        for item in items:
            print(item)

def long_notes(notes):
    return [n for n in notes if len(n) > notes_data.LONG_NOTE_LENGTH]

def short_notes(notes):
    return [n for n in notes if len(n) <= notes_data.LONG_NOTE_LENGTH]

def upper_notes(notes):
    return [n.upper() for n in notes]

def lower_notes(notes):
    return [n.lower() for n in notes]

def random_tip():
    number = random.randint(1, 3)

    if number == 1:
        print(notes_data.TIP_1)
    elif number == 2:
        print(notes_data.TIP_2)
    else:
        print(notes_data.TIP_3)

def main():
    notes = []
    tags = {}

    print(notes_data.APP_NAME)
    print("Введите help для просмотра списка команд")

    while True:
        user_input = input("\nВведите команду: ").strip()

        if user_input.startswith("add "):
            text = user_input[4:].strip()
            add_note(notes, text)
            print("Заметка добавлена")

        elif user_input.startswith("find "):
            word = user_input[5:].strip()
            found = find_note(notes, word)
            if len(found) == 0:
                print("Ничего нет")
            for idx, note in found:
                print(f"{idx + 1}: {note}")

        elif user_input.startswith("tag "):
            # parts[0] - номер заметки; parts[1] - тег
            parts = user_input[4:].split(maxsplit=1)
            if int(parts[0]) < 1 or int(parts[0]) > len(notes):
                print("Заметки с таким номером нет")
            else:
                add_tag(tags, int(parts[0]) - 1, parts[1].strip())
                print("Тег добавлен")

        elif user_input == "tags":
            all_tags = get_all_tags(tags)
            if all_tags:
                print(", ".join(sorted(all_tags)))
            else:
                print("Тегов нет")

        elif user_input == "list":
            list_notes(notes, tags)

        elif user_input == "long":
            print_list(long_notes(notes))

        elif user_input == "short":
            print_list(short_notes(notes))

        elif user_input == "upper":
            print_list(upper_notes(notes))

        elif user_input == "lower":
            print_list(lower_notes(notes))

        elif user_input == "clear":
            notes.clear()
            tags.clear()
            print("Заметки очищены")

        elif user_input == "tip":
            random_tip()

        elif user_input == "help":
            show_help()

        elif user_input == "exit":
            print("Выход...")
            break

        else:
            print("Неизвестная команда. Введите help для просмотра списка команд")

if __name__ == "__main__":
    random.seed(233393)
    main()
