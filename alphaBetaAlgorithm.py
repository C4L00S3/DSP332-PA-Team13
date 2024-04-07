def alphaBetaAlgorithm(self, gameTree: GameTree):
    def alphaBeta(node: Node, depth: int, alpha: float, beta: float, maximizingPlayer: bool):
        # Base case: depth limit reached or node is a leaf node
        if depth == 0 or len(node.children) == 0:
            self.evaluateLeafNode(node)  # Evaluate and assign heuristic value to the node
            return node.heuristicValue

        if maximizingPlayer:
            value = float('-inf')
            for child in node.children:
                # Recursive call for child nodes with depth decreased by 1
                value = max(value, alphaBeta(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # Beta cut-off
            return value
        else:
            value = float('inf')
            for child in node.children:
                # Recursive call for child nodes with depth decreased by 1
                value = min(value, alphaBeta(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Alpha cut-off
            return value

    bestValue = float('-inf')
    bestMoveIndex = -1
    # Define a practical depth limit for the search, e.g., 5 or based on your game complexity
    searchDepth = 5
    for child in gameTree.rootNode.children:
        # Initial call to alphaBeta with the practical depth limit
        value = alphaBeta(child, searchDepth, float('-inf'), float('inf'), False)
        if value > bestValue:
            bestValue = value
            bestMoveIndex = child.moveIndex
    return bestMoveIndex
