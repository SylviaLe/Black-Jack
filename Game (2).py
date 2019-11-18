# Sylvia Le, Khe Le, Jinhwa Lee
# 11/18/2019
# File: BlackJack.py
# The main logic flow of the game is here

from BlackJack import *
from graphics import *
from cards import *
from deck import *
from button import *

def endGame(window,_result_,_hit_,_stand_,_restart_,_exit_,text):
    #add a function to make the end-game code less repetitive
    _result_.setText(text)
    _hit_.deactivate()
    _stand_.deactivate()
    _restart_.activate()
    _exit_.activate()
    pt = window.getMouse()
    
    return True,pt

def rules():
    #create a window to show rules
    win2 = GraphWin('Black Jack Rules', 400, 400)
    win2.setCoords(0, 0, 200, 200)
    theme = Image(Point(100,100),"BJTheme4.gif")
    theme.draw(win2)

    title = Text(Point(100, 175), 'Rules:')
    title.setSize(30)
    title.setTextColor('lemon chiffon')
    title.setFace('century')
    title.setStyle('bold')
    title.draw(win2)

    #below just draw on the graphic win lines of rules
    line1 = Text(Point(100, 145), '- All number cards has face value')
    line1.setTextColor('white smoke')
    line1.setFace('calibri')
    line1.draw(win2)
    line2 = Text(Point(100, 130), '- Jack, King and Queen has the value of 10')
    line2.setTextColor('white smoke')
    line2.setFace('calibri')
    line2.draw(win2)
    line3 = Text(Point(100, 110), '- An Ace is either 1 or 11, whichever is better \nfor owner of the hand')
    line3.setTextColor('white smoke')
    line3.setFace('calibri')
    line3.draw(win2)
    line4 = Text(Point(100, 90), "- Try to get 21 or close to 21 as possible.\nDon't go over 21, or you will be 'BUSTED'")
    line4.setTextColor('white smoke')
    line4.setFace('calibri')
    line4.draw(win2)
    line5 = Text(Point(100, 70), "- Click 'Hit' to draw one more card")
    line5.setTextColor('white smoke')
    line5.setFace('calibri')
    line5.draw(win2)
    line6 = Text(Point(100, 50), "- Click 'Stand' to stop drawing card \nand start the dealer play")
    line6.setTextColor('white smoke')
    line6.setFace('calibri')
    line6.draw(win2)
    
def play():
    #create the window where the game happened
    win = GraphWin('Black Jack', 1000, 600)
    win.setCoords(0, 0, 200, 200)
    theme = Image(Point(100,100),"BJTheme3.gif") #pick a nice background for the game
    theme.draw(win)

    #draw the basic buttons
    hit = Button(win, Point(40,20), 20,10, "Hit")
    stand = Button(win, Point(80,20), 20, 10, "Stand")
    restart = Button(win, Point(120,20), 20, 10, "Restart")
    exitButton = Button(win, Point(160,20), 20, 10, "Exit")

    #A place to display the side (player-dealer), and the scores
    playerName = Text(Point(50, 75),"Player:")
    playerName.setFill("white")
    playerName.setSize(20)
    playerName.draw(win)
    
    dealerName = Text(Point(50, 175),"Dealer:")
    dealerName.setFill("white")
    dealerName.setSize(20)
    dealerName.draw(win)

    playerScore = Text(Point(63, 75),'')
    playerScore.setFill("white")
    playerScore.setSize(20)
    playerScore.draw(win)
    dealerScore = Text(Point(63, 175),'')
    dealerScore.setFill("white")
    dealerScore.setSize(20)
    dealerScore.draw(win)

    #placeholder for the result 
    result = Text(Point(100, 100),'')
    result.setSize(30)
    result.setFace("courier")
    result.setFill("gold")
    result.draw(win)

     #generate a BlackJack obj, let it have the first deal
    game = BlackJack()
    game.initDeal(win, 50, 50, 50, 150)

    playerTotal = game.evaluateHand(game.pHand)
    dealerTotal = game.evaluateHand(game.dHand)
    
    playerScore.setText(str(playerTotal))
    gameOver = False
    
    # First, check if player or dealer or both has BlackJack
    if playerTotal == 21 and dealerTotal != 21: #Player has blackjack
        gameOver,pt = endGame(win,result,hit,stand,restart,exitButton,"BLACK JACK!\nPlayer wins | Dealer loses")
        
    elif playerTotal == 21 and dealerTotal == 21: # Both player and dealer has blackjack
        gameOver,pt = (win,result,hit,stand,restart,exitButton,"It's a stand-off!")
        
    else: 
        pt = win.getMouse()
        
    inixP = 80
    inixD = 80
        
    while not restart.isClicked(pt) and not exitButton.isClicked(pt):

        while playerTotal < 21 and not stand.isClicked(pt) and not gameOver and not restart.isClicked(pt) and not exitButton.isClicked(pt): 
            if hit.isClicked(pt):
                restart.deactivate()
                exitButton.deactivate()
                game.hit(win,inixP,50)
                game.evaluateHand(game.pHand)
                inixP = inixP + 20  
            playerTotal = game.evaluateHand(game.pHand)
            playerScore.setText(str(playerTotal))
            if playerTotal >= 21: break
            pt = win.getMouse()            

        playerScore.setText(str(playerTotal))
        
        if playerTotal > 21: # Player's total gets over 21
            gameOver,pt = endGame(win,result,hit,stand,restart,exitButton,"BUSTED!\nPlayer loses | Dealer wins")
            
        elif (playerTotal == 21 or stand.isClicked(pt)) and not(gameOver): # Dealer's turn; Player's total is <= 21 from now
            dealerTotal = game.dealerPlays(win,inixD,150)
            game.Hcard.undraw()
            dealerScore.setText(str(dealerTotal))
            
            if dealerTotal > 21: # Dealer's total gets over 21
                gameOver,pt = endGame(win,result,hit,stand,restart,exitButton,"BUSTED!\nPlayer wins | Dealer loses")
                
            elif dealerTotal < playerTotal: # Dealer's total is less than player's
                gameOver,pt = endGame(win,result,hit,stand,restart,exitButton,"PLAYER HAS HIGHER VALUE!\nPlayer wins | Dealer loses")
                
            elif dealerTotal > playerTotal: # Dealer's total is greater than player's
                gameOver,pt = endGame(win,result,hit,stand,restart,exitButton,"DEALER HAS HIGHER VALUE!\nPlayer loses | Dealer wins")
                
            elif dealerTotal == playerTotal: # Both dealer and player have the same total
                gameOver,pt = endGame(win,result,hit,stand,restart,exitButton,"It's a stand-off!")
        
    if restart.isClicked(pt):
        game.pHand.clear()
        game.dHand.clear()
        win.close()
        play()
    else:
        win.close()

def main():
    #The intro screen of the game, showing Start, Exit, and Rules button
    mwin = GraphWin('Welcome to Black Jack',1000, 600) 
    mwin.setCoords(0, 0, 400, 400)
    theme = Image(Point(200,200),"BJTheme.gif")  #pick a nice background for the game
    theme.draw(mwin)

    proName = Text(Point(200,300), 'Black Jack')
    proName.setSize(30)
    proName.setFill('white')
    proName.setFace('courier')
    proName.draw(mwin)

    start = Button(mwin, Point(200,230), 50, 25, "Start")
    quitButton = Button(mwin, Point(200,200), 50, 25, "Quit")
    rule = Button(mwin, Point(200,170), 50, 25, "Rules")

    pt = mwin.getMouse()
    while not quitButton.isClicked(pt):
        if start.isClicked(pt):  #if start is clicked, then invoke the function that start the game 
            mwin.close()
            play()
            break
        elif rule.isClicked(pt): #if rule is clicked, open the rules window
            rules()
        pt = mwin.getMouse()

    mwin.close()  #close the intro window, start the game

main()






