import random
class Game:
    
    def __init__(self,size,playerList, gameTree):
        self.randomNumberList = self.createRandomList(size)
        self.playerList = playerList
        self.gameTree = gameTree
        self.replay = False

    def setReplay(self, replay):
        self.replay = replay
    def getReplay(self):
        return self.replay
        
    def getPlayerList(self):
        return self.playerList
    
    def setPlayerList(self, newPlayerList):
        self.playerList = newPlayerList
    
    def getGameTree(self):
        return self.gameTree
        
    def setGameTree(self, newGameTree):
        self.gameTree = newGameTree

    def getRandomNumberList(self):
        return self.randomNumberList
    def setRandomNumberList(self, newRandomNumberList):
        self.randomNumberList = newRandomNumberList
    
    def createRandomList(self, size):
        #testList = [2, 4, 7, 5, 1]
        self.randomNumberList = [random.randint(1, 9) for x in range(size)] #testList
        return self.randomNumberList
    
    def gameOver(self):
        if len(self.randomNumberList) < 2:
            return True
        else:
            return False
    
    def move(self,index,player):
        sum = self.randomNumberList[index-1]+self.randomNumberList[index]
        score = 0
        
        if(sum>7):
            score = 1
            self.randomNumberList[index-1] = 1
        elif(sum<7):
            score = -1
            self.randomNumberList[index-1] = 3
        else:
            score=2
            self.randomNumberList[index-1] = 2
        
        self.randomNumberList.pop(index)
        player.setScore(score)
