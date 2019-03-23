from enum import Enum


class Suit(Enum):
    # enum super class is inherited by sub class suit
    Spade = 1
    Heart = 2
    Diamond = 3
    Club = 4

    def __str__(self):
        # this method returns the name of the suit
        return self.name


class Rank(Enum):
    # enum super class is inherited by sub class rank

    N2 = 2
    N3 = 3
    N4 = 4
    N5 = 5
    N6 = 6
    N7 = 7
    N8 = 8
    N9 = 9
    N10 = 10
    Jack = 11
    Queen = 12
    King = 13
    ace = 14

    def __str__(self):
        # method is overriding which returns the name
        if self.value <= 10:
            return str(self.value)
        return self.name


class Card:
    # this class is used to return the suit and rank number
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        return '{} {}'.format(self.suit, self.number)


cards = [Card(suit, number) for suit in Suit for number in Rank]
# list comprehension of cards

# this loop is to print the cards in sorted form
for card in cards:
    print(card)
