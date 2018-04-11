def MCUCT(State s

):
node = s.deepcopy()
while true:
    # select based on best UCT or expand if more nodes are left unexplored
    n = TreePolicy(node)
    # simulate and backpropogate
    reward = Simulate(n)
    Update(n, reward)
return BestUCTChild(node).pos()  # return pos function required


def TreePolicy(State s

):
while next(s) != null:
    if notFullyExpanded(s):  # make this function
        return Expand(s)  # make this too
    else:
        s = BestUCTChild(s)  # code this
return s


def Expand(State s

):
return unexploredChild(s)  # code this


def Simulate(State s

):
while !goal(s):
    s = rndNext(s)  # code this function include the switch between players
return result(s)  # code this


def Update(State s, reward

):
while s != null:
    s.N += 1
    s.Q += reward
    s = parent(s)  # chech this backpropogate and code this function


def BestUCTChild(s):
    max = 0
    tbr = null
    for child in s.children():  # add children() method to state representation or code new class node
        if child.value > max:
            # put UCT function and value in state representation or code new class node
            max = child.value
            tbr = child
    return tbr


def main():
    # start with black
    turn = 1

    # define strating state of board
    start_board = State()
    start_board[3][3] = -1
    start_board[4][4] = -1
    start_board[3][4] = 1
    start_board[4][3] = 1

    board = start_board

    while !goal(board):  # code goal()

        # call for action
        i, j = MCUCT(board)  # code MCUT()

        # check if skip is happening !
        if i == NULL:
            if turn == 1:
                turn = -1
        # if it is give the chance to opponent ; code opponent()
        board = opponent(board, turn)
        else:
        turn = 1
    board = opponent(board, turn)

    else:
    # play your chance ; code Next_state()
    board = Next_state(board, turn)
    board = opponent(board)  # give your chance to opponent now


print("game finished")
print("Result: ")

if _name_ == '__main__':
    main()
