from peewee import *

db = PostgresqlDatabase('flashcards', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Flashcard(BaseModel):
    front = CharField()
    back = CharField()
    times_correct = IntegerField()
    times_missed = IntegerField()
    

db.connect()

def translate():  
    db.drop_tables([Flashcard])
    db.create_tables([Flashcard])
    card1 = Flashcard(front="buenos dias", back="good morning", times_correct = 0, times_missed=0)
    card1.save()
    card2 = Flashcard(front="buenas tardes", back="good afternoon", times_correct = 0, times_missed=0)
    card2.save()
    card3 = Flashcard(front="buenas noches", back="good evening", times_correct = 0, times_missed=0)
    card3.save()
    card4 = Flashcard(front="hola, mi nombre es ____", back="hi my name is", times_correct = 0, times_missed=0)
    card4.save()
    card5 = Flashcard(front="como estas?", back="how are you?", times_correct = 0, times_missed=0)
    card5.save()
    card6 = Flashcard(front="con permiso", back="excuse me", times_correct = 0, times_missed=0)
    card6.save()
    card7 = Flashcard(front="gracias", back="thank you", times_correct = 0, times_missed=0)
    card7.save()
    card8 = Flashcard(front="salud", back="bless you", times_correct = 0, times_missed=0)
    card8.save()
    card9 = Flashcard(front="de nada", back="you're welcome", times_correct = 0, times_missed=0)
    card9.save()
    card10 = Flashcard(front="que hora es", back="what time is it", times_correct = 0, times_missed=0)
    card10.save()
    card11 = Flashcard(front="si", back="yes", times_correct = 0, times_missed=0)
    card11.save()
    card12 = Flashcard(front="lo siento", back="I'm sorry", times_correct = 0, times_missed=0)
    card12.save()
    card13 = Flashcard(front="como se llama usted", back="what's your name", times_correct = 0, times_missed=0)
    card13.save()
    card14 = Flashcard(front="adios", back="goodbye", times_correct = 0, times_missed=0)
    card14.save()
    card15 = Flashcard(front="hola", back="hello", times_correct = 0, times_missed=0)
    card15.save()
    card16 = Flashcard(front="estoy bien", back="I'm fine", times_correct = 0, times_missed=0)
    card16.save()
    card17 = Flashcard(front="por favor", back="please", times_correct = 0, times_missed=0)
    card17.save()
    card18 = Flashcard(front="cuando", back="when", times_correct = 0, times_missed=0)
    card18.save()
    card19 = Flashcard(front="como", back="how", times_correct = 0, times_missed=0)
    card19.save()
    card20 = Flashcard(front="cuanto", back="how many", times_correct = 0, times_missed=0)
    card20.save()
    