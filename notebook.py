from datetime import datetime
import json



notes = []



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
    

def add_note():
    new_note = input_data()
    max_id = max(note['id'] for note in notes) if notes else 0
    new_note['id']= max_id + 1
    notes.append(new_note)

    
def print_notebook():
    print(notes)

add_note()
add_note()
print_notebook()



