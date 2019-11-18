# Sylvia Le, Khe Le, Jinhwa Lee
# 11/18/2019
# File: BlackJack.py
# The basics moves in BlackJack

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
          """Create a deck of cards, then shuffle it
             Set the initial list to contains the hands of both player and dealer later
          """
          self.deck = Deck()   
          self.deck.shuffle()
          self.dHand = dHand
          self.pHand = pHand
          self.Hcard = Image(Point(50, 150), 'b2fv.gif')
          
     def initDeal(self, window, xposP, yposP, xposD, yposD):
         #Distribute the first two cards to the player and the dealer. Generate the coords at which the card will be drawn
          #Hide the first card of the dealer
         
          x = 0     
          hole = True #the first card is the card that needed to be hiden
          for i in range(2):
               initP = self.deck.dealCard()  #get the value of the next card
               Pcard = Image(Point((xposP + x), yposP), initP.getImgFile())  #draw it on the graphic windows
               Pcard.draw(window)
               self.pHand.append(initP)  #add the card to list of hands
                 
               initD = self.deck.dealCard()   #get the value of the next card
               Dcard = Image(Point((xposD + x), yposD), initD.getImgFile())  #draw it on the graphic window
               Dcard.draw(window)
               self.dHand.append(initD)
               if hole:
                    self.Hcard.draw(window) #hide the first card, by drawing an image over it
                    hole = False

               x = x + 10  #increment the value of x, so that the second card will not be drawn over the first
               
     def hit(self, window, xPos,yPos):
          """Give the user one more card when they click 'Hit'
             Draw it on the graphic window
          """
          newCard = self.deck.dealCard()
          newimg = Image(Point(xPos, yPos), newCard.getImgFile())
          newimg.draw(window)
          self.pHand.append(newCard)  #add this new card into the list of hand
          
     def evaluateHand(self, hand):
          """Calculate the total value of the hands 
             Evaluate the value of the Ace card
          """
          total = 0
          ace = False  #suppose at first we don't know if the Ace is there

          for card in hand:
               if card.getValue() == 1: #if there is a card with the value of 1, then player/dealer have an Ace
                    ace = True
               total = total + card.getValue()

          if ace and total + 10 <= 21:  #Evaluate the value of Ace, if set the value as 11 make the total larger than 21 then it has the value of 1
               total = total + 10

          return total

     def dealerPlays(self, window, xPos, yPos):
          """Let the dealer deal cards
             Draw the cards on the graphics window
          """
          total = 0
          total = self.evaluateHand(self.dHand)

          while total < 17:  #while the total value is still smaller than 17, then continue dealing cards
               newDCard = self.deck.dealCard()
               self.dHand.append(newDCard)
               total = self.evaluateHand(self.dHand)
               Dimg = Image(Point(xPos,yPos), newDCard.getImgFile())
               Dimg.draw(window)

               xPos = xPos + 10  #increment value of x so that new card will not be drawn over
          return total
          
def main():  #just a test to make sure things are working okay
     win = GraphWin('Test', 800, 600)
     win.setCoords(0, 0, 200, 200)
     win.setBackground('lavender')

     bj = BlackJack()
     bj.initDeal(win, 25, 25, 25, 75)

     win.getMouse()
     win.close()
               

if __name__ == '__main__':
     main()
            
        
