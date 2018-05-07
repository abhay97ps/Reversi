import numpy as np
import random
import copy
from Model.ModelHelper import Next, Check


class Node:
    turn = 0
    N = 0  # number of simulations
    Q = 0  # number of wins
    C = 1  # weight given to exploration
    parent = None
    state = None
    Children = []  # list of node class
    UnexploredChildren = []  # list of node class
    ExploredChildren = []  # list of node class

    def __init__(self, state, turn):
        self.turn = turn
        self.state = state

    def getChildren(self):
        c = Next(self.state, self.turn)
        Children = []
        for child in c:
            new_node = Node(child, switch(self.turn))
            Children.append(new_node)
        if not self.Children:
            self.Children = copy.deepcopy(Children)
            self.UnexploredChildren = copy.deepcopy(Children)
            self.ExploredChildren = []

    def UCTValue(self):
        return float((self.Q / self.N) + self.C * np.sqrt(np.log(self.N) / self.N))

    def getState(self):
        return self.state

    def notFullyExpanded(self):
        if self.UnexploredChildren:
            return True
        else:
            return False

    def randomNext(self):
        if self.Children:
            return random.choice(self.Children)
        else:
            return self.skip()

    def skip(self):
        return Node(self.state, switch(self.turn))

    def unexploredChild(self):
        child = random.choice(self.UnexploredChildren)
        self.UnexploredChildren.remove(child)
        return child

    def isNotTerminal(self):
        if Check(self.state, self.turn) or Check(self.state, switch(self.turn)):      # condition for non-terminal
            return True
        else:
            return False


def switch(val):
    if val == 1:
        return -1
    elif val == -1:
        return 1
