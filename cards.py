from random import randrange
from graphics import *

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.imgfile =  self.__str__() + '.gif'

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def getValue(self):
        if self.rank <= 10:
            return self.rank
        else:
            return 10
        
    def __str__(self):
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
    
    def getImgFile(self):
        return self.imgfile

def main():
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
