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

    listSize = 0
    indexActualPlayer = 0
    chosenAlgorithm = 0

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
            game_gui.displayGameScreen(game_gui.master, game)
            game_gui.displayList(initialNumberList)
            game_gui.displayActualPlayer(indexActualPlayer)
            playGame(root, game_gui, game, indexActualPlayer, chosenAlgorithm, playerList)

    check_game_info()

    root.mainloop()

    """#input size
  game = Game(17,playerList,None)
  while(game.gameOver() != True):
  #input index
  game.move(1,human)
  #ai algorythm
  #game.move(6,computer)
  #update gui"""


def playGame(root, game_gui, game, indexActualPlayer, chosenAlgorithm, playerList):
    def checkHasPlayed(root, indexActualPlayer, playerList):
        if game_gui.getHasPlayed() == False:
            # Check again after 1 second
            root.after(1000, checkHasPlayed(root, indexActualPlayer, playerList))
        else:
            #while game.gameOver() != True:
            for i in range(0, 1):
                if indexActualPlayer == 0:
                    # get the index from the player from the gui
                    indexToMerge = game_gui.getIndex()
                    print("Index: ", indexToMerge)
                    game.move(indexToMerge, game.getPlayerList()[indexActualPlayer])
                    newNumberList = game.getRandomNumberList()
                    indexActualPlayer = 1
                    game_gui.setHasPlayed(False)
                    game_gui.updateGUI(newNumberList, indexActualPlayer, playerList)

                elif (indexActualPlayer == 1):
                    # get the index from the player from the gui
                    indexToMerge = game_gui.getIndex()
                    print("Index: ", indexToMerge)
                    game.move(indexToMerge, game.getPlayerList()[indexActualPlayer])
                    newNumberList = game.getRandomNumberList()
                    indexActualPlayer = 0
                    game_gui.setHasPlayed(False)
                    game_gui.updateGUI(newNumberList, indexActualPlayer, playerList)

    checkHasPlayed(root, indexActualPlayer, playerList)


main()
