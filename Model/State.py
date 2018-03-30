import numpy as np
from Bot.Heuristic import evaluate


class State:
    Board = np.zeros((8, 8))
    Value = 0
    # The two types of pieces
    Black = 1
    Whtie = -1

    def __init__(self, board):
        self.Board = board
        self.Value = self.value()

    def value(self):
        return evaluate(self.Board)
