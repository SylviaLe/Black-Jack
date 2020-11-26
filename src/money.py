from button import Button
from graphics import *

class Money():
    """Attributes of this Money class are as follows.
       INSTANCE VARIABLES
        cash: amount of cash that player owns
        betAmount: amount of bets that player places"""         
    def __init__(self,initCash):
        self.cash = initCash
        self.betAmount = 0

    def cashOut(self,value):
        """Place bets on the table"""
        if value <= self.cash:
            self.betAmount += value
            #self.cash -= value

    def cashBack(self,value):
        """Put bets back"""
        self.cash += value
        self.betAmount -= value
        
    def win(self):
        """Add cash to player's account if she wins"""
        self.cash += self.betAmount * 2
        self.betAmount = 0
        
    def lose(self):
        """Take cash from player's account if she loses"""
        self.cash -= self.betAmount
        self.betAmount = 0

    def push(self):
        """Put bets back if she mades a stand-off"""
        self.cash += self.betAmount
        self.betAmount = 0

