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
    def check_game_info():
        if game_gui.getHasChosen() == False:
            # Check again after 1 second
            root.after(1000, check_game_info)
        else:
            gameInformationList = game_gui.getGameInfo()
            listSize = gameInformationList[0]
            indexActualPlayer = gameInformationList[1]
            chosenAlgorithm = gameInformationList[2]

            game = Game(listSize, playerList, None)
            initialNumberList = game.getRandomNumberList()

            # display initial state of the game
            game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
            playGame(root, game_gui, game, indexActualPlayer, chosenAlgorithm, playerList)

    check_game_info()

    root.mainloop()
def playGame(root, game_gui, game, indexActualPlayer, chosenAlgorithm, playerList):
    def checkHasPlayed(root, indexActualPlayer, playerList):
        if game_gui.getHasPlayed() == False:
            print("on est ICI, has played: ", game_gui.getHasPlayed())
            # Check again after 1 second
            root.after(1000, checkHasPlayed,root, indexActualPlayer, playerList)
        else:
            return 1
            """"#for i in range(0, 1):
                if indexActualPlayer == 0:
                    # get the index from the player from the gui
                    indexToMerge = game_gui.getIndex()
                    print("Index: ", indexToMerge)
                    game.move(indexToMerge, game.getPlayerList()[indexActualPlayer])
                    game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
                    indexActualPlayer = 1
                    game_gui.setHasPlayed(False)
                    print("Has played: ", game_gui.getHasPlayed())
                    return indexActualPlayer

                elif (indexActualPlayer == 1):
                    # get the index from the player from the gui
                    indexToMerge = game_gui.getIndex()
                    print("Index: ", indexToMerge)
                    game.move(indexToMerge, game.getPlayerList()[indexActualPlayer])
                    game_gui.setHasPlayed(False)
                    game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
                    indexActualPlayer = 0
                    print("Has played: ", game_gui.getHasPlayed())"""
    while not game.gameOver():

        value = checkHasPlayed(root, indexActualPlayer, playerList)
        while value != 1:
            if indexActualPlayer == 0:
                # get the index from the player from the gui
                indexToMerge = game_gui.getIndex()
                print("Index: ", indexToMerge)
                game.move(indexToMerge, game.getPlayerList()[indexActualPlayer])
                game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
                indexActualPlayer = 1
                game_gui.setHasPlayed(False)
                print("Has played: ", game_gui.getHasPlayed())
                return indexActualPlayer

            elif (indexActualPlayer == 1):
                # get the index from the player from the gui
                indexToMerge = game_gui.getIndex()
                print("Index: ", indexToMerge)
                game.move(indexToMerge, game.getPlayerList()[indexActualPlayer])
                game_gui.setHasPlayed(False)
                game_gui.displayGameScreen(game_gui.master, game, indexActualPlayer, playerList)
                indexActualPlayer = 0
                print("Has played: ", game_gui.getHasPlayed())
        value = 0




main()
