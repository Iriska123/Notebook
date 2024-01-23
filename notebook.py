from datetime import datetime
import json


notes = {}


def input_data():
    note = {}
    user_title = input("Введите название заметки: ")
    user_text = input("Введите текст заметки: ")
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    note['id'] = 0
    note['title'] = user_title
    note['text']= user_text
    note['date'] = current_datetime
    return note
    

def file_append(data):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open("notebook.json", "a+", encoding="UTF-8") as file:
        # for note in notes:
            json.dump(data, file,indent=4)

def add_note():
    temp_note = {}
    temp_data = input_data()
    if not notes:
        id = 0
        notes[id] = temp_data
        temp_note[id] = temp_data
        file_append(temp_note)

    else:
        max_id = max(notes.keys())
        max_id += 1
        notes[max_id] = temp_data
        temp_note[max_id] = temp_data
        file_append(temp_note)
 
    
    # file_append(notes)
 

    
def print_notebook():
    print(notes)

add_note()
print_notebook()
add_note()
# add_note()
print_notebook()



