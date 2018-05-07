import numpy as np


class State:
    Board = np.zeros((8, 8))
    # The two types of pieces/players
    Black = 1
    White = -1

    def __init__(self, board):
        if board is None:
            self.Board[3][3] = -1
            self.Board[4][4] = -1
            self.Board[3][4] = 1
            self.Board[4][3] = 1
        else:
            self.Board = board

    def result(self):
        v = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if self.Board[i][j] == 1:
                    v += 1
                elif self.Board[i][j] == -1:
                    v += -1
                else:
                    v += 0
        if v > 0:
            return 1  # Black won
        if v < 0:
            return -1  # White won
        if v == 0:
            return 0
