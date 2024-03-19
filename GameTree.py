from typing import Optional,List
from copy import deepcopy

class State:
    def __init__(self,numbers:list, playerScore:int, computerScore:int) -> None:
        self.numbers = numbers
        self.playerScore = playerScore
        self.computerScore = computerScore

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value,State):
            pass
        return self.numbers == __value.numbers and self.playerScore == __value.playerScore and self.computerScore == __value.computerScore

class Node:
    depth = 0
    def __init__(self,state:State,parent: Optional['Node'] = None):
        self.state = state
        self.parent = parent
        self.children:List[Node] = []
        if(parent!=None):
            self.depth=parent.depth+1

    def expand(self):
        
        if(self.isTerminal()):
            return 
        for x in range(len(self.state.numbers)-1):
            stateCopy = deepcopy(self.state)
            nextState = self.makeMove(x,stateCopy)
            if(self.checkSameChildState(nextState)):
                continue
            self.children.append(Node(nextState,self))

    def makeMove(self,index:int,state:State):
        number = state.numbers[index]+state.numbers[index+1]
        score = 0
        if(number>7):
            score = 1
            state.numbers[index] = 1
        elif(number<7):
            score = -1
            state.numbers[index] = 3
        else:
            score=2
            state.numbers[index] = 2
        if(self.depth%2==0):
            state.playerScore+=score
        else:
            state.computerScore+=score

        state.numbers.pop(index+1)
        return state
    
    def showNodeTree(self, indent=0):
        print("| " * indent + str(self))
        for child in self.children:
            child.showNodeTree(indent + 1)

    def isTerminal(self):
        return len(self.state.numbers)==1
    def __repr__(self):
        stringToReturn = "Player Score: {}, Computer Score: {}, Numbers: {}".format(self.state.playerScore,self.state.computerScore,self.state.numbers)
        return repr(stringToReturn)

    def checkSameChildState(self,nextState:State)->bool:
        for child in self.children:
            if(child.state == nextState):
                return True
        return False

class GameTree:
    def __init__(self,initialState:State):
        self.rootNode = Node(initialState)
        self.nodeCount = 0

    def expand(self,node:Node,depth):
        node.expand()
        self.nodeCount+=1
        for child in node.children:
            if(child.depth!=depth):
                self.expand(child,depth)

    def findNode(self,state:State,start:Node)->Node:
        visited = set()
        stack = [start]
        while(stack):
            node = stack.pop()
            if(node.state == state):
                return node
            if node not in visited:
                visited.add(node)
                stack.extend(node.children)
