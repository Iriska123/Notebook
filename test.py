from datetime import datetime
import json
import uuid
import csv



# def read_json():
#     with open('notebook.json', 'r') as file:
#         content = file.read()
#         return json.load(content)
    

def input_data():
   
    note = {}
    user_title = input("Введите название заметки: ")
    user_text = input("Введите текст заметки: ")
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    note['id'] = str(uuid.uuid4())
    note['title'] = user_title
    note['text']= user_text
    note['date'] = current_datetime
    return note

    
def csv_append():
    with open('notebook.csv', 'a+', newline='') as file:
        fieldnames = ['id', 'title','text','date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(input_data())

def csv_reader():
    with open('notebook.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        notes = []
        for row in reader:
            notes.append(', '.join(row))
    return notes


def csv_print():
    notes = csv_reader()
    print(notes)
        

def find_note(str):
    notes = csv_reader()
    temp = []
    for note in notes:
        temp.append(note)
    for el in range(len(temp)):
        string = temp[el]
        index = string.find(str)
        if index != -1:
            print(string)
            

def change_note():
    notes = csv_reader()
    temp = []
    for note in notes:
        temp.append(note)
    for el in range(len(temp)):
        string = temp[el]
        index = string.find(str)
        if index != -1:
            find_note = string



# csv_append()
# csv_print()
find_note('sobaka')
# print(csv_reader())