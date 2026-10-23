notes = ""

while True:
    user_input = input("Введите команду: ")

    if user_input.startswith("add "):
        if notes == "":
            notes = notes + user_input[4:] 
        else:
            notes = notes + "\n" + user_input[4:]
        print("Заметка добавлена")
    
    if user_input.startswith("find "):
        if user_input[5:] in notes:
            print("Найдено")
        else:
            print("Не найдено")

    if user_input == "list":
        print(notes)

    if user_input == "clear":
        notes = ""
        print("Заметки очищены")

    if user_input == "exit":
        break