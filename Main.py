from AI import AI
from Player import Player
from GUI import GUI
from class_game import Game
import tkinter as tk
from GameTree import GameTree,State
import time



def main():
    # create the window for the gui
    root = tk.Tk()
    game_gui = GUI(root)
    # create the two players and player list
    human = Player()
    computer = AI()
    playerList = [human, computer]
    game_gui.displayStartGameScreen()
    checkStartInfo(game_gui, root, playerList)
    root.mainloop()


def checkStartInfo(game_gui, root, playerList):
    if game_gui.getHasChosen() == False:
        # Check again after 1 second
        root.after(1000, checkStartInfo, game_gui, root, playerList)
    else:
        gameInformationList = game_gui.getGameInfo()
        listSize = gameInformationList[0]
        indexActualPlayer = gameInformationList[1]
        chosenAlgorithm = gameInformationList[2]
        game = Game(listSize, playerList, None)
        game_gui.setIndexActualPlayer(indexActualPlayer)
        game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
        checkPlayInfo(game_gui, root, game, indexActualPlayer, chosenAlgorithm, playerList)


def checkPlayInfo(game_gui, root, game, indexActualPlayer, chosenAlgorithm, playerList):
    if game_gui.getHasPlayed() == False:
        print("on est ICI, has played: ", game_gui.getHasPlayed())
        #root.after(1000, checkPlayInfo, game_gui, root, game, indexActualPlayer, chosenAlgorithm, playerList)
    else:
        if game_gui.getIndexActualPlayer() == 0:
            # get the index from the player from the gui
            indexToMerge = game_gui.getIndex()
            game.move(indexToMerge, game.getPlayerList()[game_gui.getIndexActualPlayer()])
            game_gui.setIndexActualPlayer(1)
            game_gui.setHasPlayed(False)
            if game.gameOver():
                endGame(game_gui, game,root)
            else:
                game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)

        elif game_gui.getIndexActualPlayer() == 1:
            if game_gui.getGameInfo()[1] == 1:
                isMax = True
            else:
                isMax = False
            if chosenAlgorithm == 0:
                human = game.getPlayerList()[0]
                computer = game.getPlayerList()[1]
                tree = GameTree(State(game.getRandomNumberList(), human.getScore(), computer.getScore()), 3, 0)
                time.sleep(2)
                computerIndex = computer.minimaxAlgorithm(tree)
                print("Computer chose to merge index: ", computerIndex)
                game.move(computerIndex, computer)
                game_gui.setIndexActualPlayer(0)
                game_gui.setHasPlayed(False)
                if game.gameOver():
                    endGame(game_gui, game, root)
                else:
                    game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList, AIChoice=str(computerIndex+1))
            elif chosenAlgorithm == 1:
                human = game.getPlayerList()[0]
                computer = game.getPlayerList()[1]
                tree = GameTree(State(game.getRandomNumberList(), human.getScore(), computer.getScore()), 5, 0)
                time.sleep(1)
                computerIndex = computer.alphaBetaAlgorithm(tree, isMax)
                game.move(computerIndex, computer)
                print("Computer chose to merge index: ", computerIndex)
                game_gui.setIndexActualPlayer(0)
                game_gui.setHasPlayed(False)
                if game.gameOver():
                    endGame(game_gui, game, root)
                else:
                    game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList, AIChoice=str(computerIndex+1))

    if not game.gameOver():
        root.after(1000, checkPlayInfo, game_gui, root, game, indexActualPlayer, chosenAlgorithm, playerList)
    else:
        endGame(game_gui, game, root)

def endGame(game_gui, game, root):
    game_gui.displayEndGameScreen(game)
    if game.getReplay() == True:
        #fermer la fenetre
        game_gui.master.destroy()
        main()
    else:
        root.after(1000, endGame, game_gui, game, root)


if __name__ == '__main__':
    main()
