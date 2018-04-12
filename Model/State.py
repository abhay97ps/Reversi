import numpy as np


class State:
    Board = np.zeros((8, 8))
    Value = 0
    # The two types of pieces/players
    Black = 1
    White = -1

    def __init__(self, board):
        self.Board = board
        self.Value = self.value()

    def value(self):
        value = 0
        # to do quantify state
        for i in range(0, 8):
            for j in range(0, 8):
                if self.Board[i][j] == 1:
                    value += 1
                elif self.Board[i][j] == -1:
                    value += -1
                else:
                    value += 0
        if value > 0:
            return 1        # Black won
        else:
            return -1       # White won
