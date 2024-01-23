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
    )

def createFrontCard():
    pass

def createBackCard():
    pass 