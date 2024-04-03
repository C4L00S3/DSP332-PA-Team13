from typing import Optional, List
from enum import Enum

class Turn(Enum):
    MAX = 0
    MIN = 1

class State:
    def __init__(self, numbers: List[int], playerScore: int, computerScore: int) -> None:
        self.numbers = numbers
        self.playerScore = playerScore
        self.computerScore = computerScore

    def apply_move(self, index: int) -> None:
        number = self.numbers[index] + self.numbers[index + 1]
        if number > 7:
            score = 1
            self.numbers[index] = 1
        elif number < 7:
            score = -1
            self.numbers[index] = 3
        else:
            score = 2
            self.numbers[index] = 2
        if node.turn == Turn.MAX:
            self.playerScore += score
        else:
            self.computerScore += score
        self.numbers.pop(index + 1)

class Node:
    def __init__(self, state: State, parent: Optional['Node'] = None, moveIndex=0):
        self.moveIndex = moveIndex
        self.state = state
        self.parent = parent
        self.depth = parent.depth + 1 if parent else 0
        self.turn = Turn.MAX if self.depth % 2 == 0 else Turn.MIN
        self.children_generator = self.generate_children()

    def generate_children(self):
        if not self.is_terminal():
            for x in range(len(self.state.numbers) - 1):
                next_state = State(self.state.numbers[:], self.state.playerScore, self.state.computerScore)
                next_state.apply_move(x)
                if not self.check_same_child_state(next_state):
                    yield Node(next_state, self, x)

    def is_terminal(self):
        return len(self.state.numbers) == 1

    def check_same_child_state(self, next_state: State) -> bool:
        current_node = self.parent
        while current_node:
            if current_node.state == next_state:
                return True
            current_node = current_node.parent
        return False

class GameTree:
    def __init__(self, initial_state: State, depth_limit):
        self.root_node = Node(initial_state)
        self.node_count = 1
        self.depth_limit = depth_limit

    def find_node(self, state: State, start: Node) -> Node:
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node.state == state:
                return node
            if node not in visited:
                visited.add(node)
                stack.extend(node.children_generator)


