#thisfilename: game.py

#Error: getMouse in closed window
#Tell the user that once you start playing(hit or stand), you cannot restart or exit the game

from BlackJack import *
from graphics import *
from cards import *
from deck import *
from button import *

def endGame(window,_result_,_hit_,_stand_,_restart_,_exit_,text):
    _result_.setText(text)
    _hit_.deactivate()
    _stand_.deactivate()
    _restart_.activate()
    _exit_.activate()
    pt = window.getMouse()
    
    return True,pt
    
def play():

    win = GraphWin('Black Jack', 1000, 600)
    win.setCoords(0, 0, 200, 200)
    theme = Image(Point(100,100),"BJTheme3.gif") #or BJTheme2 if you like
    theme.draw(win)

    hit = Button(win, Point(40,20), 20,10, "Hit")
    stand = Button(win, Point(80,20), 20, 10, "Stand")
    restart = Button(win, Point(120,20), 20, 10, "Restart")
    exitButton = Button(win, Point(160,20), 20, 10, "Exit")

    playerName = Text(Point(50, 75),"Player:")
    playerName.setFill("white")
    playerName.setSize(20)
    playerName.draw(win)
    
    dealerName = Text(Point(50, 175),"Dealer:")
    dealerName.setFill("white")
    dealerName.setSize(20)
    dealerName.draw(win)

    playerScore = Text(Point(60, 75),'')
    playerScore.setFill("white")
    playerScore.setSize(20)
    playerScore.draw(win)
    dealerScore = Text(Point(60, 175),'')
    dealerScore.setFill("white")
    dealerScore.setSize(20)
    dealerScore.draw(win)
    result = Text(Point(100, 100),'')
    result.setSize(30)
    result.setFace("courier")
    result.setFill("gold")
    result.draw(win)

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
                
            elif ealerTotal == playerTotal: # Both dealer and player have the same total
                gameOver,pt = endGame(win,result,hit,stand,restart,exitButton,"It's a stand-off!")
        
    if restart.isClicked(pt):
        game.pHand.clear()
        game.dHand.clear()
        win.close()
        play()
    else:
        win.close()

def main():

    mwin = GraphWin('Welcome to Black Jack',1000, 600)
    mwin.setCoords(0, 0, 400, 400)
    theme = Image(Point(200,200),"BJTheme.gif")
    theme.draw(mwin)

    proName = Text(Point(200,300), 'Black Jack')
    proName.setSize(30)
    proName.setFill('white')
    proName.setFace('courier')
    proName.draw(mwin)

    rules = Text(Point(200,150), 'enter rules here')
    rules.setFill('white')
    rules.setSize(20)
    rules.draw(mwin)

    start = Button(mwin, Point(200,230), 50, 25, "Start")
    quitButton = Button(mwin, Point(200,200), 50, 25, "Quit")

    pt = mwin.getMouse()
    while not quitButton.isClicked(pt):
        if start.isClicked(pt):
            mwin.close()
            play()
        pt = mwin.getMouse()

    mwin.close()  

main()






