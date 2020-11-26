from BlackJack import *
from graphics import *
from cards import *
from deck import *
from button import *

def intro():
    win1 = GraphWin('Welcome to Black Jack', 1000, 600)
    win1.setCoords(0, 0, 400, 400)
    theme = Image(Point(200,200),"theme/BJTheme.gif")
    theme.draw(win1)

    proName = Text(Point(200,300), 'Black Jack')
    proName.setSize(36)
    proName.setTextColor('white')
    proName.setFace('century')
    proName.draw(win1)

    start = Button(win1, Point(200,230), 50, 25, "Start")
    Quit = Button(win1, Point(200,200), 50, 25, "Quit")
    rule = Button(win1, Point(200,170), 50, 25, "Rules")

    pt = win1.getMouse()
    while not Quit.isClicked(pt):
        if start.isClicked(pt):
            win1.close()
            main()
            break
        elif rule.isClicked(pt):
            rules()
            
        pt = win1.getMouse()

    win1.close()  

def rules():
    win2 = GraphWin('Black Jack Rules', 400, 400)
    win2.setCoords(0, 0, 200, 200)
    theme = Image(Point(100,100),"theme/BJTheme4.gif")
    theme.draw(win2)

    title = Text(Point(100, 175), 'Rules:')
    title.setSize(30)
    title.setTextColor('lemon chiffon')
    title.setFace('century')
    title.setStyle('bold')
    title.draw(win2)

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
    
def main():
    win = GraphWin('Black Jack', 1000, 600)
    win.setCoords(0, 0, 200, 200)
    theme = Image(Point(100,100),"theme/BJTheme3.gif") 
    theme.draw(win)

    hit = Button(win, Point(40,20), 20,10, "Hit")
    stand = Button(win, Point(80,20), 20, 10, "Stand")
    restart = Button(win, Point(120,20), 20, 10, "Restart")
    Exit = Button(win, Point(160,20), 20, 10, "Exit")
    

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

    dealerScore = Text(Point(65, 175),'')
    dealerScore.setFill("white")
    dealerScore.setSize(20)
    dealerScore.draw(win)

    result = Text(Point(100, 100),'')
    result.setSize(30)
    result.setFace("calibri")
    result.setStyle('bold')
    result.setFill("gold")
    result.draw(win)

    game = BlackJack()
    game.initDeal(win, 50, 50, 50, 150)

    playerScore.setText(str(game.evaluateHand(game.pHand)))

    if game.evaluateHand(game.pHand) == 21 and game.evaluateHand(game.dHand) != 21:
        result.setText('BLACK JACK! You Win!')
        hit.deactivate()
        stand.deactivate()
    if game.evaluateHand(game.pHand) == 21 and game.evaluateHand(game.dHand) == 21:
        game.Hcard.undraw()
        result.setText("It's  a Stand-off")
        hit.deactivate()
        stand.deactivate()
    pt = win.getMouse()
    inixP = 70
    inixD = 70
    #while not Exit.isClicked(pt):
    while not Exit.isClicked(pt):

        if hit.isClicked(pt):
            game.hit(win, inixP, 50)
            playerScore.setText(str(game.evaluateHand(game.pHand)))
            inixP = inixP + 10

            if game.evaluateHand(game.pHand) == 21:
                if game.evaluateHand(game.pHand) == game.evaluateHand(game.dHand):
                    game.Hcard.undraw()
                    result.setText('PUSH! It\'s a tie!')
                    hit.deactivate()
                    stand.deactivate()
                else:
                    game.Hcard.undraw()
                    result.setText('You Win')
                    hit.deactivate()
                    stand.deactivate()

            elif game.evaluateHand(game.pHand) > 21:
                game.Hcard.undraw()
                result.setText('BUSTED! You lose')
                hit.deactivate()
                stand.deactivate()
                
        elif stand.isClicked(pt):
            game.dealerPlays(win, inixD, 150)
            dealerScore.setText(str(game.evaluateHand(game.dHand)))
            inixD = inixD + 10

            if game.evaluateHand(game.dHand) > 21:
                game.Hcard.undraw()
                result.setText('DEALER BUSTED! You wins')
                hit.deactivate()
                stand.deactivate()
            elif game.evaluateHand(game.pHand) == 21 and game.evaluateHand(game.dHand) == 21:
                game.Hcard.undraw()
                result.setText('PUSH! It\'s a tie!')
                hit.deactivate()
                stand.deactivate()
            else:
                if game.evaluateHand(game.dHand) < game.evaluateHand(game.pHand):
                    game.Hcard.undraw()
                    result.setText('You score is greater, you win')
                    hit.deactivate()
                    stand.deactivate()
                elif game.evaluateHand(game.dHand) > game.evaluateHand(game.pHand):
                    game.Hcard.undraw()
                    result.setText('You score is lower, you lose')
                    hit.deactivate()
                    stand.deactivate()
                else:
                    game.Hcard.undraw()
                    result.setText('PUSH! It\'s a tie!')
                    hit.deactivate()
                    stand.deactivate()

        elif restart.isClicked(pt):
            game.dHand.clear()
            game.pHand.clear()
            win.close()
            main()
            break
        pt = win.getMouse()
    win.close()
intro()
