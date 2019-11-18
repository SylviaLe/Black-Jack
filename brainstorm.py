#questions: number of people in game, does the dealer draw card and what the hell,
"""about stages of designing:
1, generate random cards:
https://www.slader.com/textbook/9781590282410-python-programming-an-introduction-to-computer-science-2nd-edition/279/programming-exercises/11/
https://www.slader.com/textbook/9781590282410-python-programming-an-introduction-to-computer-science-2nd-edition/280/programming-exercises/12/

2, generate deck class
constructor: Creates a new deck of 52 cards in a standard order.
shufe: Randomizes the order of the cards.
dealCard: Returns a single card from the top of the deck and removes the
card fom the deck.
cardsLeft: Returns the number of cards remaining in the deck.

3, blackjack class
 METHODS
       
        __init__(self, dHand=[], pHand=[])
            constructor that initializes instance variables
            it also gives the playingDeck an initial shuffle
            indicate the interface to call from (eg: class BJInterface)
            e.g. self.interface = BJInterface()
        initDeal(self,gwin,xposD,yposD,xposP,yposP):
            deals out initial cards, 2 per player and 
            displays dealer and player hands on graphical win
            xposD and yposD give initial position for dealer cards
            xposP and yposP are analogous
        hit(self, gwin, xPos, yPos)
            adds a new card to the player's hand and places it at xPos, yPos
        evaluateHand(self, hand)
            totals the cards in the hand that is passed in and returns total
            (ace counts as 11 if doing so allows total to stay under 21)
        dealearPlays(self, gwin, xPos, yPos)
            dealer deals cards to herself, stopping when hitting "soft 17"
    https://codereview.stackexchange.com/questions/177523/simple-oop-blackjack-game-in-python
4, interface


4, other extra stuff
- make the graphics more beautiful
- face down
- play again
- money
- high score keeper
- double down and splitting """


