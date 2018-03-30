def evaluate(board):
    value = 0
    # to do quantify state
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == 1:
                value += 1
            elif board[i][j] == -1:
                value += -1
            else:
                value += 0
    return value
