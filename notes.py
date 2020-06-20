from peewee import *
import click

db = PostgresqlDatabase('notetaker', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField()
    contents = TextField()


db.drop_tables([Note])
db.create_tables([Note])

note1 = Note(title='Note1', contents='This is the first note')
note1.save()

note2 = Note(title='Note2', contents='This is the second note')
note2.save()

note3 = Note(title='Note3', contents='This is the third note')
note3.save()

note4 = Note(title='Note4', contents='This is the fourth note')
note4.save()













# @click.group()
# @click.version_option(version='1.0.0', prog_name='NoteTaker')

# def main():
#     """Hi! I'm Note Taker, I'm here to help you take Notes!""" 

#     pass

# # Create notes

# @main.command()
# @click.option('--title','-ti',prompt=True)
# @click.option('--contents', '-cont',prompt=True)

# def add_note(title):
#     """ Add a New Note """

#     print(title)

# def add_contents(contents):
#     """ Add New Contents to Note """

#     print(contents)

# Read notes
# Select specific note


# if __name__ == "__main__":
#     main()
    # db.connect()
    # db.create_tables([Note])