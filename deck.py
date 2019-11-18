# Sylvia Le, Khe Le, Jinhwa Lee
# 11/18/2019
# File: BlackJack.py
# Generate a deck of card, and the behaviors it has

from cards import Card
from random import *
class Deck:
    def __init__(self):
        """INSTANCE VARS: self.cards: a list of all the cards in the deck"""
        self.cards = []
        for s in ['c', 's', 'd', 'h']:
            for r in range(1, 14):
                self.cards.append(Card(s, r)) #append the card to the list 

    def shuffle(self):
        """Shuffle all the cards in the deck"""
        shuffle(self.cards)
        return self.cards

    def dealCard(self):
        """Pop out the first card in the deck that has been shuffled"""
        return self.cards.pop(0)

    def cardLeft(self):
        """Return the number of card left in the deck"""
        return str(len(self.cards))

def main():  #Just a test to see if things is going well
    deck = Deck()
    deck.shuffle()
    card = deck.dealCard()
    print(card)
    print(deck.cardLeft())

if __name__ == "__main__":
    main()

        

