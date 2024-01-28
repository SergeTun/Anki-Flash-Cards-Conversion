import genanki
import os
import string
import re
import random

def noteFormat():
    note_format = genanki.model(
        random.randrange(1 << 30, 1 << 31),
        'Simple Model',
        fields =[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates = [
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ]
    return note_format
    )   

def createNotes(note_format, file_contents):
    my_note = genanki.note(
        model = note_format,
        fields=[file_contents]
    )

def process_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
        
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read



def main():
    userName = os.getlogin()
    folder_path = rf'C:\Users\{userName}\Desktop\Anki_Converter'