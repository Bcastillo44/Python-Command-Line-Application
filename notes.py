
from collections import OrderedDict
import datetime
import sys
import os
# import click

from peewee import *


db = PostgresqlDatabase('notetaker', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    # title = CharField()
    contents = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)


def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Note], safe=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
    """Show the Menu"""
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

# def add_title():
#     """Add a Title."""
#     print("Enter your Title.")
#     data = sys.stdin.read().strip()

#     if data:
#         if input('Save Title? [Yn] ').lower() == 'y':
#             Note.create(title=data)
#             print("Saved successfully!")


def add_note():
    """Add a New Note."""
    print("Enter your Note. Press Ctrl+D when finished.")
    data = sys.stdin.read().strip()

    if data:
        if input('Save Note? [Yn] ').lower() != 'n':
            Note.create(contents=data)
            print("Saved successfully!")


def view_notes(search_query=None):
    """View Previous Notes."""
    notes = Note.select().order_by(Note.timestamp.desc())

    if search_query:
        notes = notes.where(Note.contents.contains(search_query))

    for note in notes:
        timestamp = note.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(note.contents)
        print('\n\n'+'='*len(timestamp))
        print('n) next note')
        print('d) delete note')
        print('q) return to main menu')

        next_action = input('Action: [Ndq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_note(note)


def search_notes():
    """Search notes."""
    view_notes(input('Search query: '))

def delete_note(note):
    """Delete a Note."""
    if input("Are you sure? [yN] ").lower() == 'y':
        note.delete_instance()
        print("Note deleted!")


menu = OrderedDict([
    # ('t', add_title),
    ('a', add_note),
    ('v', view_notes),
    ('s', search_notes),
])


if __name__ == '__main__':
     initialize()
     menu_loop()

