import genanki
import os
import io
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

def createNotes(note_format):
    my_note = genanki.note(
        model = note_format,
        fields=[]
    )

def process_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file_name in files:
        if file_name.endswith('txt'):
            pass

def main():
    userName = os.getlogin()
    folder_path = rf'C:\Users\{userName}\Desktop\Anki_Converter'