# Sylvia Le, Khe Le, Jinhwa Lee
# 11/18/2019
# File: BlackJack.py
# With methods to return the basic properties of a card in a deck

from random import randrange
from graphics import *

class Card:
    """INSTANCE VARS:
    - the card's suit
    - the card's rank
    - the name of the file that match with the card name
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.imgfile = 'img/' + self.__str__() + '.gif'  #the file name of the card

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def getValue(self):
        if self.rank <= 10:
            return self.rank #if the card is not K, Q or J, has face value
        else:
            return 10  #K, Q, J has value of 10
        
    def __str__(self):
        # generate a string that represent the card
        ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        suits = ['c', 's', 'd', 'h']
        if self.suit == 'c':
            cardName = suits[0] + ranks[self.rank - 1] 
        elif self.suit == 's':
            cardName = suits[1] + ranks[self.rank - 1] 
        elif self.suit == 'd':
            cardName = suits[2] + ranks[self.rank - 1] 
        else:
            cardName = suits[3] + ranks[self.rank - 1] 
        return cardName  
        #since we need the file name more, we don't write want to write out the full name of the card

    def getImgFile(self):
        return self.imgfile  #return the file name of the matching card

def main():  #just a testing site
    win = GraphWin('Cards', 600, 600)
    win.setCoords(0, 0, 20, 20)
    win.setBackground('lavender')
    
    for i in range(1,4):
        cardRank = randrange(1, 14)
        cardSuit = ['c', 's', 'd', 'h']
        ind = randrange(4)
        card = Card(cardSuit[ind], cardRank)
        print(card)
    
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
