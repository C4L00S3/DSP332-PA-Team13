class Game:
    
    def __init__(self,size,playerList, gameTree):
        self.randomNumberList = createRandomList(size)
        self.playerList = playerList
        self.gameTree = gameTree
        
    def getPlayerList(self):
        return self.playerList
    
    def setPlayerList(self, newPlayerList):
        self.playerList = newPlayerList
    
    def getGameTree(self):
        return self.gameTree
        
    def setGameTree(self, newGameTree):
        self.gameTree = newGameTree
    
    def createRandomList(self, size):
        import random
        else:
            self.randomNumberList = [random.randint(1, 9) for x in range(size)]
            return self.randomNumberList
    
    def gameOver(self, numberList):
        if len(numberList) == 2:
            return True
        else:
            return False
