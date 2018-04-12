import numpy as np
import random
from Model.ModelHelper import *


def switch(val):
    if val == 1:
        return -1
    elif val == -1:
        return 1


class Node:
    turn = 0
    UCTValue = 0.0
    N = 0  # number of simulations
    Q = 0  # number of wins
    C = 1  # weight given to exploration
    parent = None
    state = None
    Children = []               # list of state class
    UnexploredChildren = []     # list of state class
    ExploredChildren = []       # list of node class

    def __init__(self, state, turn):
        self.turn = turn
        self.state = state
        self.Children = Next(self.state, self.turn)
        self.UnexploredChildren = self.Children

    def UCTUpdate(self):
        return (self.Q / self.N) + self.C * np.sqrt(np.log(self.N) / self.N)

    def getState(self):
        return self.state

    def notFullyExpanded(self):
        if len(self.UnexploredChildren) != 0:
            return True
        else:
            return False

    def randomNext(self):
        return Node(random.choice(self.Children), switch(self.turn))

    def unexploredChild(self):
        child = random.choice(self.UnexploredChildren)
        self.UnexploredChildren.remove(child)
        self.ExploredChildren.append(Node(child, switch(self.turn)))
        return Node(child, switch(self.turn))

    def isNotTerminal(self):
        if len(self.Children) == 0 and len(Next(self.state, switch(self.turn))) == 0:   # condition for terminal
            return False
        else:
            return True

    def result(self):
        if not self.isNotTerminal():
            return self.state.Value
