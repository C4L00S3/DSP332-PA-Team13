from AI import AI
from Player import Player
from GUI import GUI
from class_game import Game
import tkinter as tk


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
            print("INDEX FIRST PLAYER = ", indexActualPlayer)
            game = Game(listSize, playerList, None)
            game_gui.setIndexActualPlayer(indexActualPlayer)
            game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
            if game_gui.getIndexActualPlayer() == 1:
                game_gui.setIndexActualPlayer(0)
            else:
                game_gui.setIndexActualPlayer(1)
            checkPlayInfo(game_gui, root, game, indexActualPlayer, chosenAlgorithm, playerList)

def checkPlayInfo(game_gui, root, game, indexActualPlayer, chosenAlgorithm, playerList):
    if game_gui.getHasPlayed() == False:
        print("on est ICI, has played: ", game_gui.getHasPlayed())
        # Check again after 1 second
        root.after(1000, checkPlayInfo, game_gui, root, game, indexActualPlayer, chosenAlgorithm, playerList)
    else:
        if game_gui.getIndexActualPlayer() == 0:
            # get the index from the player from the gui
            indexToMerge = game_gui.getIndex()
            print("Index: ", indexToMerge)
            game.move(indexToMerge, game.getPlayerList()[game_gui.getIndexActualPlayer()])
            game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
            game_gui.setIndexActualPlayer(1)
            game_gui.setHasPlayed(False)
            print("Has played: ", game_gui.getHasPlayed())
            print("Index actual player: ", game_gui.getIndexActualPlayer())

        elif game_gui.getIndexActualPlayer() == 1:
            # get the index from the player from the gui
            indexToMerge = game_gui.getIndex()
            print("Index: ", indexToMerge)
            game.move(indexToMerge, game.getPlayerList()[indexActualPlayer])
            game_gui.setHasPlayed(False)
            game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
            game_gui.setIndexActualPlayer(0)
            print("Has played: ", game_gui.getHasPlayed())
            print("Index actual player: ", game_gui.getIndexActualPlayer())

        # Check if the game is over
        if not game.gameOver():
            # If the game is not over, call checkPlayInfo again after 1 second
            root.after(1000, checkPlayInfo, game_gui, root, game, indexActualPlayer, chosenAlgorithm, playerList)
if __name__ == '__main__':
    main()
