from Bot.MCUCT import MCUCT
from Model.ModelHelper import Check
from Model.State import State

Black = 1
White = -1


def switch(val):
    if val == Black:
        return White
    elif val == White:
        return Black


def gameOver(state):
    if Check(state, Black) or Check(state, White):
        return False
    else:
        return True


def main():
    turn = Black  # start with black

    start_board = State(None)  # define starting state of board
    game_state = start_board
    print(game_state.Board)
    while not gameOver(game_state):
        if Check(game_state, turn):
            game_state = MCUCT(game_state, turn)
        turn = switch(turn)
        print(game_state.Board)

    if game_state.result() == 1:
        print('winner is Black')
    elif game_state.result() == -1:
        print('winner is White')
    else:
        print('draw')


if __name__ == '__main__':
    main()
