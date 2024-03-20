from Player import Player
from GameTreeTest import GameTree,Node,Turn
from typing import List
from collections import deque

class AI(Player):

  def evaluateNodes(self,leafNodes:List[Node]):
    queue:deque[Node] = deque()
    visited = set()

    queue.extend(leafNodes)

    while queue:
      currentNode = queue.pop()

      if len(currentNode.children)==0:
        currentNode.heuristicValue = currentNode.state.playerScore-currentNode.state.computerScore
      else:
        if(currentNode.turn == Turn.MAX):
          currentNode.heuristicValue = max(currentNode.getChildrenValues())
        else:
          currentNode.heuristicValue = min(currentNode.getChildrenValues())
      visited.add(currentNode)
      if not currentNode.parent:
        return
      queue.appendleft(currentNode.parent)

  
  def pickIndex(self,gameTree:GameTree):
    bestMove = gameTree.rootNode
    for child in gameTree.rootNode.children:
      if child.heuristicValue == bestMove.heuristicValue:
        bestMove = child
    return bestMove.moveIndex
      

  def findLeafNodes(self,gameTree:GameTree)->List[Node]:
    visited = set()
    stack = [gameTree.rootNode]
    leafNodes = []
    while(stack):
      node = stack.pop()
      if(len(node.children)==0):
          leafNodes.append(node)
      if node not in visited:
          visited.add(node)
          stack.extend(node.children)
    return leafNodes

  def minimaxAlgorithm(self,gameTree:GameTree)->int:
    self.evaluateNodes(self.findLeafNodes(gameTree))
    return self.pickIndex(gameTree)
    

  def alphaBetaAlgorithm(gameTree:GameTree)->int:
    pass
