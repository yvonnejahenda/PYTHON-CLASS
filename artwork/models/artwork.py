from peewee import (CharField SqliteDatabase,
Model,TextField,IntegerField,OperationalError,
IntegrityError)
db = SqliteDatabase("Artwork.db")



class Artwork(Model):
    
    name = CharField(max_length=1000,unique=True)
    description=TextField(default="Good image")
    thumbnail_link = CharField(max_length=1000)
    fullimage_link=CharField(max_length=1000)


    class Meta:
        database = db


def initialize():
    try:
      Artwork.create_table()
    except OperationalError:
        pass
        Artwork.create(
          name="monkey_singing",
          description="Awesome Artistic Monkey",
          thumbnail_link="https://artwork--yvonnejahendah.repl.co/static/music-3507317_640.jpg",
          fullimage_link="https://artwork--yvonnejahendah.repl.co/static/music-3507317_1920.jpg"
        )
        except IntegrityError:
          pass
    