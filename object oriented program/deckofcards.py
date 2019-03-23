import itertools
import random


def deck_cards():
    # This method is used to shuffle the deck of cards


    deck_cards = list(itertools.product(
        ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen',  'king', 'ace'],
        ['spades', 'clubs', 'diamonds', 'hearts']))
    # This itertools module  standardizes a core set of fast, memory efficient tools that are useful in combination.
    print(deck_cards)

    for number_of_players in range(1, 5):
        # This loop shuffle cards to 4 players
        random.shuffle(deck_cards)
        # random.shuffle" is used to shuffle the cards
        print("\n")
        print("player = ", number_of_players, " got these cards \n")

        for number_of_cards in range(1, 14):
            # This loop is to distribute 13 cards to the players
            print(number_of_cards, deck_cards[number_of_cards][0], " of ", deck_cards[number_of_cards][1])




Cards_object = deck_cards()
# Card object is created

if __name__ == '__main__':
    deck_cards()
    # Deck of cards method is called
