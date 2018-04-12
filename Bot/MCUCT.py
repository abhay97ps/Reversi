import null
from Bot.BotHelper import *
from Bot.Node import Node


def MCUCT(state, turn):
    node = Node(state, turn)            # take care of turn
    while resourceIsAvailable():        # define criteria as req
        n = TreePolicy(node)            # select based on best UCT or expand if more nodes are left unexplored
        reward = Simulate(n)            # simulate and back propagate
        Update(n, reward)
    return BestUCTChild(node)           # return pos function required


def TreePolicy(node):
    while len(node.Children) != 0:
        if node.notFullyExpanded():
            return Expand(node)
        else:
            node = BestUCTChild(node)
    return node


def Expand(node):
    new_node = node.unexploredChild()
    new_node.parent = node
    return new_node


def Simulate(node):
    while node.isNotTerminal():         # include all three in node class definition
        node = node.randomNext()
    return node.result()                # code this


def Update(node, reward):
    while node is not None:
        node.N += 1
        node.Q += reward                # win +1 loss -1
        node = node.parent              # check this back propagate and code this function in node class


def BestUCTChild(node):
    Max = 0
    tbr = null
    for child in node.ExploredChildren:       # add children() method to  class node
        child.UCTUpdate()               # update the UCT value
        if child.value > Max:
            Max = child.value           # put UCT function and value in state representation or code new class node
            tbr = child
    return tbr


'''
def main():
    # start with black
    turn = 1

    # define starting state of board
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


if __name__ == '__main__':
    main()
'''