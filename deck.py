from cards import Card
from random import *
class Deck:
    def __init__(self):
        self.cards = []
        for s in ['c', 's', 'd', 'h']:
            for r in range(1, 14):
                self.cards.append(Card(s, r))

    def shuffle(self):
        shuffle(self.cards)
        return self.cards

    def dealCard(self):
        return self.cards.pop(0)

    def cardLeft(self):
        return str(len(self.cards))

def main():
    deck = Deck()
    deck.shuffle()
    card = deck.dealCard()
    print(card)
    print(deck.cardLeft())

if __name__ == "__main__":
    main()

        

