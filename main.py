import random
import notes_data


def show_help():
    print("add текст - добавить заметку")
    print("find слово - найти текст в заметках")
    print("list - показать все заметки")
    print("clear - удалить все заметки")
    print("tip - получить случайную подсказку")
    print("exit - завершить программу")


def add_note(notes, text):
    if notes == "":
        return text
    return notes + notes_data.NOTE_SEPARATOR + text


def list_notes(notes):
    if notes == "":
        print("Список заметок пуст.")
    else:
        print(notes)


def find_note(notes, word):
    if word in notes:
        return "Найдено"
    else:
        return "Не найдено"


def random_tip():
    number = random.randint(1, 3)

    if number == 1:
        print(notes_data.TIP_1)
    elif number == 2:
        print(notes_data.TIP_2)
    else:
        print(notes_data.TIP_3)


def main():
    notes = ""

    print(notes_data.APP_NAME)
    print("Введите help, чтобы посмотреть команды.")

    while True:
        user_input = input("\nВведите команду: ").strip()

        if user_input.startswith("add "):
            text = user_input[4:].strip()
            notes = add_note(notes, text)
            print("Заметка добавлена")

        elif user_input.startswith("find "):
            word = user_input[5:].strip()
            print(find_note(notes, word))

        elif user_input == "list":
            list_notes(notes)

        elif user_input == "clear":
            notes = ""
            print("Заметки очищены")

        elif user_input == "tip":
            random_tip()

        elif user_input == "help":
            show_help()

        elif user_input == "exit":
            print("Выход...")
            break

        else:
            print("Неизвестная команда. Введите help для просмотра команд.")


if __name__ == "__main__":
    random.seed(2333)
    main()
