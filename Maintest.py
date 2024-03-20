from AItest import AI 
from GameTreeTest import GameTree,State
from class_game import Game
from Player import Player


def update():
    print(game.getRandomNumberList())
    print(human.getScore())
    print(computer.getScore())

computer = AI()
human = Player()
playerList = [human,computer]
TREE_DEPTH = 3
game = Game(20,playerList,None)
while not game.gameOver():
    update()
    humanIndex = int(input("Input index: "))
    game.move(humanIndex,human)
    print(game.getRandomNumberList())
    tree = GameTree(State(game.getRandomNumberList(),human.getScore(),computer.getScore()),TREE_DEPTH)
    computerIndex = computer.minimaxAlgorithm(tree)
    game.move(computerIndex,computer)
    print("Computer chose to merge index: ",computerIndex)


