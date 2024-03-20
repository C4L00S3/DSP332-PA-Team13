from AI import AI 
from GameTree import GameTree,State,Node
from copy import deepcopy

def main():
    computer = AI()
    startNums = [2,7,8,4,8,2,3,7,8,5,2,7,9,5,4]
    initialState = State(startNums.copy(),0,0)
    treeDepth = 3
    tree = GameTree(deepcopy(initialState))
    tree.expand(tree.rootNode,treeDepth)
    #tree.rootNode.showNodeTree()
    #nextNode = tree.findNode(State([1, 8, 5, 7, 1, 9, 4, 8, 4, 6, 1, 6],2,1),tree.rootNode)
    #tree = GameTree(nextNode.state)
    #tree.expand(tree.rootNode,treeDepth)
    computer.evaluateNodes(computer.findLeafNodes(tree))
    tree.rootNode.showNodeTree()
    print(computer.pickIndex(tree))
    #nextNode = tree.findNode(State([1, 5, 7, 9, 3, 1],1,3),nextNode)
    #tree.expand(nextNode,treeDepth+3)
    print(tree.nodeCount)
main()