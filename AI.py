from Player import Player
from GameTree import GameTree,Node,Turn
from typing import List
from collections import deque

class AI(Player):

  def evaluateLeafNode(self,currentNode:Node):
    if currentNode.state.playerScore>currentNode.state.computerScore:
          currentNode.heuristicValue=1
    elif currentNode.state.playerScore<currentNode.state.computerScore:
          currentNode.heuristicValue=-1
    else:
          currentNode.heuristicValue=0

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
    queue:deque[Node] = deque()
    visited = set()
    queue.extend(self.findLeafNodes(gameTree))
    while queue:
      currentNode = queue.pop()
      if len(currentNode.children)==0:
        self.evaluateLeafNode(currentNode)
      else:
        if(currentNode.turn == Turn.MAX):
          currentNode.heuristicValue = max(currentNode.getChildrenValues())
        else:
          currentNode.heuristicValue = min(currentNode.getChildrenValues())
      visited.add(currentNode)
      if not currentNode.parent:
        break
      queue.appendleft(currentNode.parent)
    return self.pickIndex(gameTree)

  def alphaBetaAlgorithm(self, gameTree, isMax):
      def alphaBeta(node, depth, alpha, beta, maximizingPlayer):
          if depth == 0 or len(node.children) == 0:
              self.evaluateLeafNode(node)
              return node.heuristicValue

          if maximizingPlayer:
              value = float('-inf')
              for child in node.children:
                  value = max(value, alphaBeta(child, depth - 1, alpha, beta, maximizingPlayer))
                  alpha = max(alpha, value)
                  if alpha >= beta:
                      break  # Beta cut-off
              return value
          else:
              value = float('inf')
              for child in node.children:
                  value = min(value, alphaBeta(child, depth - 1, alpha, beta, maximizingPlayer))
                  beta = min(beta, value)
                  if beta <= alpha:
                      break  # Alpha cut-off
              return value

      bestValue = float('-inf')
      bestMoveIndex = -1
      for child in gameTree.rootNode.children:
          value = alphaBeta(child, float('inf'), float('-inf'), float('inf'), isMax)
          if value > bestValue:
              bestValue = value
              bestMoveIndex = child.moveIndex
      return bestMoveIndex
