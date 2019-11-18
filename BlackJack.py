from button import *
from cards import *
from deck import *
from graphics import *
from random import *

class BlackJack:
     
     
     """Attributes of this Blackjack class are as follows.
       INSTANCE VARIABLES

        dealerHand: a list of PlayingCard objects representing the dealer's hand
        playerHand: a list of PlayingCard objects representing the player's hand
        playingDeck: a Deck object representing the deck of cards the game is being played with"""

     def __init__(self, dHand = [], pHand = []):

          self.deck = Deck()
          self.deck.shuffle()
          self.dHand = dHand
          self.pHand = pHand
          self.Hcard = Image(Point(50, 150), 'b2fv.gif')
          
     def initDeal(self, window, xposP, yposP, xposD, yposD):
         
          x = 0
          hole = True
          for i in range(2):
               initP = self.deck.dealCard()
               Pcard = Image(Point((xposP + x), yposP), initP.getImgFile())
               Pcard.draw(window)
               self.pHand.append(initP)
                 
               initD = self.deck.dealCard()
               Dcard = Image(Point((xposD + x), yposD), initD.getImgFile())
               Dcard.draw(window)
               self.dHand.append(initD)
               if hole:
                    self.Hcard.draw(window)
                    hole = False

               x = x + 10
               
     def hit(self, window, xPos,yPos):
          
          newCard = self.deck.dealCard()
          newimg = Image(Point(xPos, yPos), newCard.getImgFile())
          newimg.draw(window)
          self.pHand.append(newCard)
          
     def evaluateHand(self, hand):
          total = 0
          ace = False

          for card in hand:
               if card.getValue() == 1:
                    ace = True
               total = total + card.getValue()

          if ace and total + 10 <= 21:
               total = total + 10

          return total

     def dealerPlays(self, window, xPos, yPos):
          total = 0
          total = self.evaluateHand(self.dHand)

          while total < 17:
               newDCard = self.deck.dealCard()
               self.dHand.append(newDCard)
               total = self.evaluateHand(self.dHand)
               Dimg = Image(Point(xPos,yPos), newDCard.getImgFile())
               Dimg.draw(window)

               xPos = xPos + 10
          return total
          
def main():
     win = GraphWin('Test', 800, 600)
     win.setCoords(0, 0, 200, 200)
     win.setBackground('lavender')

     bj = BlackJack()
     bj.initDeal(win, 25, 25, 25, 75)

     win.getMouse()
     win.close()
               

if __name__ == '__main__':
     main()
            
        
