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
        if len(numberList) == 1:
            return True
        else:
            return False
    
    def move(self,index,player):
        sum = game.randomNumberList[index]+game.randomNumberList[index+1]
        score = 0
        
        if(sum>7):
            score = 1
            game.randomNumberList[index] = 1
        elif(sum<7):
            score = -1
            game.randomNumberList[index] = 3
        else:
            score=2
            game.randomNumberList[index] = 2
        
        game.randomNumberList.pop(index+1)
        player.add_score(score)
