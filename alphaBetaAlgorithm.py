def alphaBetaAlgorithm(self, gameTree: GameTree):
    def alphaBeta(node: Node, depth: int, alpha: float, beta: float, maximizingPlayer: bool):
   
        if depth == 0 or len(node.children) == 0:
            self.evaluateLeafNode(node)  
            return node.heuristicValue

        if maximizingPlayer:
            value = float('-inf')
            for child in node.children:
             
                value = max(value, alphaBeta(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  
            return value
        else:
            value = float('inf')
            for child in node.children:
               
                value = min(value, alphaBeta(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    break  
            return value

    bestValue = float('-inf')
    bestMoveIndex = -1

    searchDepth = 5
    for child in gameTree.rootNode.children:
      
        value = alphaBeta(child, searchDepth, float('-inf'), float('inf'), False)
        if value > bestValue:
            bestValue = value
            bestMoveIndex = child.moveIndex
    return bestMoveIndex
