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

from translations import translate
import random

db.drop_tables([Flashcard])
db.create_tables([Flashcard])

translate()


print("\n BIENVENIDXS! What would you like to do?")

def train():
    
    action = input("\n * 'create' to create a new card, \n * 'view' to view your deck of cards', \n * 'train' to review your cards. ")
    
    if action == "create" or action == "Create":
        new_card = input("What Spanish word or phrase would you like to practice? Type in all lowercase. ")
        new_translation = input("And its English translation? Type in all lowercase. ")
        new = Flashcard(front=new_card, back=new_translation, times_correct = 0, times_missed=0)
        new.save()
        print(f'{new.front} / translation: {new.back}')
        train()

    elif action == "view" or action == "View":
        for flashcard in Flashcard.select():
            print(f"{flashcard.front} / translation: {flashcard.back} / times correct: {flashcard.times_correct} / times missed: {flashcard.times_missed}")
        train()

    elif action == "train" or action == "Train":
        print("\n * Each turn, you will be presented with a word or phrase in Spanish. \n * Return its translation in English. Type in all lowercase!")

        deck = list(Flashcard.select())

        random.shuffle(deck)

        cardstack = int(
            input("\nHow many cards would you like to review? Choose up to 20. "))
        
        while cardstack > 20 or cardstack < 1:
            cardstack = int(input("\nNope! Please choose a number between 1 and 20."))

        print("\nWrite 'quit' at any time to finish your review sesh.")

        for i in range(0, cardstack, 1):

            response = input(deck[i].front+" / translation: ")

            if response == 'quit':
                print("\nHasta luego!")
                exit()

            elif response == deck[i].back:
                deck[i].times_correct = deck[i].times_correct + 1
                deck[i].save()
                print("\nMuy bien! \nYou've answered this correctly {} times.".format(deck[i].times_correct))

            elif response != deck[i].back:
                deck[i].times_missed = deck[i].times_missed + 1
                deck[i].save()
                print("\nNope! \nYou've missed this one {} times.".format(deck[i].times_missed))

            if i == (cardstack - 1):
                review_again = input(
                    "You've reached the end of this session. Back to the main menu, y/n?")
                if review_again == "Y" or review_again == "y":
                    train()
                else:
                    print("Hasta luego!")
                break

train()
