from AI import AI 
from GameTree import GameTree,State
from class_game import Game
from Player import Player


def update():
    print(game.getRandomNumberList())
    print("Human score : ",human.getScore())
    print("IA Score : ", computer.getScore())

computer = AI()
human = Player()
playerList = [human,computer]
TREE_DEPTH = 5
game = Game(20,playerList,None)
liste = [2, 4, 7, 5, 1]
game.setRandomNumberList(liste)
while not game.gameOver():
    print("Liste: ",game.getRandomNumberList())
    humanIndex = int(input("Input index: "))
    game.move(humanIndex,human)
    print(game.getRandomNumberList())

    tree = GameTree(State(game.getRandomNumberList(), human.getScore(), computer.getScore()), TREE_DEPTH, 0)
    computerIndex = computer.alphaBetaAlgorithm(tree)
    game.move(computerIndex, computer)
    print("Computer chose to merge index: ", computerIndex)
    update()

    """tree = GameTree(State(game.getRandomNumberList(),human.getScore(),computer.getScore()),TREE_DEPTH, 0)
    computerIndex = computer.minimaxAlgorithm(tree)
    game.move(computerIndex,computer)
    print("Computer chose to merge index: ",computerIndex)"""


