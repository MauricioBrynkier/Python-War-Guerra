import random
from tabnanny import check
from tkinter import Y
from typing import Type


values = {'Dos':2, 'Tres':3, 'Cuatro':4, 'Cinco':5, 'Seis':6, 'Siete':7, 'Ocho':8, 'Nueve':9, 'Diez':10, 'Sota':11, 'Reina':12, 'Rey':13, 'As':14}
#Los valores de las cartas del juego
suits = ('Corazones', 'Diamante', 'Pica', 'Trebol')
#El palo de la carta
ranks = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Sota', 'Reina', 'Rey', 'As')
#El rango de los valores

class Card:        
#Se crea la clase de cartas para poder tener el valor de cada carta junto a su palo
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.rank + " de " + self.suit

class Deck:

    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)

    def shuffle(self):
        
        random.shuffle(self.all_cards)

    def __str__(self):

        for card in self.all_cards:
            print(card)


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):

        return self.all_cards.pop(0)

    def add_cards(self,new_cards):

        if type(new_cards) == type([]):
            
            self.all_cards.extend(new_cards)
            

        else:
            self.all_cards.append(new_cards)


    def __str__(self):
        
        return f'El jugador {self.name} tiene {len(self.all_cards)} cartas'


def logica():

    nombre1 = 'Mauri'#input('Ingrese el nombre del primer jugador:\n')
    nombre2 = 'Joaco'#input('Ingrese el nombre del segundo jugador:\n')
    jugador1 = Player(nombre1)
    jugador2 = Player(nombre2)

    new_deck = Deck()
    new_deck.shuffle()

    for i in range(26):
        
        jugador1.add_cards(new_deck.all_cards.pop(0))
        jugador2.add_cards(new_deck.all_cards.pop(0))

    

    while len(jugador1.all_cards) != 0 and len(jugador2.all_cards) != 0:

        
        print(f'{jugador1.name} levanto la carta {jugador1.all_cards[0]}')
        print(f'{jugador2.name} levanto la carta {jugador2.all_cards[0]}\n')
        print(jugador1)
        print(f'{jugador2}\n')
        
        cartas = []
        cartas.append(jugador1.remove_one())
        cartas.append(jugador2.remove_one())
        
        

        

        while True:

            numcarta = len(cartas)

            if values[cartas[numcarta-2].rank] > values[cartas[numcarta-1].rank]:
                random.shuffle(cartas)
                jugador1.add_cards(cartas)
                print(f'{jugador1.name} gano\n')
                
                break
                

            elif values[cartas[numcarta-2].rank] < values[cartas[numcarta-1].rank]:
                random.shuffle(cartas)
                jugador2.add_cards(cartas)
                print(f'{jugador2.name} gano\n')
                
                break
            

            elif values[cartas[numcarta-2].rank] == values[cartas[numcarta-1].rank] :
                if len(jugador1.all_cards)< 3:
                    jugador2.all_cards.extend(jugador1.all_cards)
                    break

                elif len(jugador2.all_cards)< 3:
                    jugador1.all_cards.extend(jugador2.all_cards)
                    break
                    


                print('Guerra!!!!')
                
                for i in range(2):

                    cartas.append(jugador1.remove_one())
                    cartas.append(jugador2.remove_one())

            else:
                break

    if jugador1.all_cards!=0:

        print(f'{jugador1.name} Gano la Guerra')

    else:
        print(f'{jugador1.name} Gano la Guerra')

    juego = input("Queres volver a jugar? y = si / n = no\n")

    if juego == 'y':
        logica()

    else:
        print('Gracias por jugar')
        



logica()


