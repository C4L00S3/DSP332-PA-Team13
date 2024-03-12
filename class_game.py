class Game:
    
    def __init__(self,randomNumberList, playerList, gameTree):
        self.randomNumberList = []
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
        if size < 15 or size > 25:
            return "Wrong size. It have to be between 15 and 25"
        else:
            self.randomNumberList = [random.randint(1, 9) for x in range(size)]
            return self.randomNumberList
    
    def gameOver(self, numberList):
        if len(numberList) == 2:
            return True
        else:
            return False
