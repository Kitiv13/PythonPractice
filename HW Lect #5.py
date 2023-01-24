documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def find_people(document):
    num = input("Введите номер документа:")
    for el in document:
        if num == el["number"]:
            return el["name"]
    return "Документ введен не верно!"


def find_shelf(directorie):
    num = input("Введите номер документа:")
    for el in directorie.items():
        if num in el[1]:
            return f'Номер полки {el[0]}'
    return "Документ введен не верно!"


def get_list(document):
    for el in document:
        print(f'{el["type"]}, "{el["number"]}", {el["name"]}')


def add_doc(document, directorie):
    type = input("Введите тип документа:")
    number = input("Введите номер документа:")
    name = input("Введите Имя, Фамилию владельца:")
    shelf = input("Введите номер полки для хранения:")
    if shelf not in directorie:
        return "Полки не существует"
    if shelf in directorie:
        document.append({"type": type, "number": number, "name": name})
        directorie[shelf].append(number)
    return "Данные внесены"


def del_number(document, directorie):
    doc_len = len(document)
    number = input("Введите номер документа для удаления:")
    for k, v in enumerate(document):
        if v["number"] == number:
            document.pop(k)

    if doc_len == len(document):
        return "Документ не существует!"

    for value in directorie.values():
        if number in value:
            value.remove(number)

    return "Документ удален!"


def move_number(directorie):
    doc_number = False
    number = input("Введите номер документа, который хотите переместить:")
    shelf = input("Введите номер полки, на котрую хотите переместить:")
    if shelf not in directorie:
        return "Полки не существует!"

    for k, v in directorie.items():
        if number in v:
            doc_number = True
            directorie[shelf] += [number]
            v.remove(number)

    if doc_number:
        return "Документ перемещен!"
    else:
        return "Документ не существует"


def add_shelf(directorie):
    shelf = input("Введите номер новой полки:")
    if shelf in directorie:
        return "Полка уже существует"
    directorie[shelf] = []
    return f"Полка за номером {shelf} добавлена."


def main(document, directorie):
    print("Возможные команды: p, l, s, a, d, m, as.")
    print("Для выхода введите - q.")
    while True:
        user = input("Введите команду:")
        if user == 'p':
            print(find_people(documents))
        elif user == 'l':
            (get_list(documents))
        elif user == 's':
            print(find_shelf(directories))
        elif user == 'a':
            print(add_doc(documents, directorie))
        elif user == 'd':
            print(del_number(documents, directories))
        elif user == 'm':
            print(move_number(directories))
        elif user == 'as':
            print(add_shelf(directories))
        elif user == 'q':
            print("Работа завершена")
            break


(main(documents, directories))
