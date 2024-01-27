from datetime import datetime
import json
import uuid


def create_json():
    json_data = [{
        'id': str(uuid.uuid4()),
        'title': input("Введите название заметки: "),
        'text': input("Введите текст заметки: "),
        'date': str(datetime.now().strftime("%d-%m-%Y")),
        }
    ]
    with open('notes.json', 'w', encoding="UTF-8") as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))


def add_to_json():
    json_data = {
        'id': str(uuid.uuid4()),
        'title': input("Введите название заметки: "),
        'text': input("Введите текст заметки: "),
        'date': str(datetime.now().strftime("%d-%m-%Y")), 
    }
    data = json.load(open("notes.json"))
    data.append(json_data)
    with open("notes.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def update_json():
    search = input("Изменение заметки. Введите название заметки для поиска: ")

    data = json.load(open("notes.json"))
    for el in data:
        if el['title'] == search:
            new_title = input("Изменение заметки. Введите новое название заметки: ")
            new_text = input("Изменение заметки. Введите новый текст заметки: ")
            el['title'] = new_title
            el['text'] = new_text

    with open("notes.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
 

def search_in_json():
    new_text = input("Поиск заметки. Введите дату для поиска: ")
    data = json.load(open("notes.json"))
    for el in data:
        if el['date'] == new_text:
            print(el)


def delete_from_json():
    new_text = input("Удаление заметки. Введите название заметки для удаления: ")
    data = json.load(open("notes.json"))
    # print(type(data))
    for el in data:
            # print(el)
        if el['title'] == new_text:
            data.remove(el) 
    with open("notes.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def print_notebook():
    data = json.load(open("notes.json"))
    print(data)


create_json()
add_to_json()
update_json()
search_in_json()
delete_from_json()
print_notebook()
