from AI.py import AI
from Player.py import Player
from GUI.py import GUI
from class_game.py import Game

gui = GUI()
human = Player()
computer = AI()
playerList = [human,computer]
#input size
game = Game(17,playerList,None)
while(!game.gameOver()):
  #input index
  game.move(1,human)
  #ai algorythm
  #game.move(6,computer)
  #update gui
