import numpy as np
import copy

from Model.State import State


def North(i, j, board, turn):
    if (board[i - 1][j] == 0 or board[i - 1][j] == turn):
        return
    else:
        for k in range(i - 2, -1, -1):
            if (board[k][j] == 0):
                return [k, j]
            elif (board[k][j] == turn):
                return
            else:
                continue
        return


def East(i, j, board, turn):
    if (board[i][j + 1] == 0 or board[i][j + 1] == turn):
        return
    else:
        for k in range(j + 2, 8):
            if (board[i][k] == 0):
                return [i, k]
            elif (board[i][k] == turn):
                return
            else:
                continue
        return


def South(i, j, board, turn):
    if (board[i + 1][j] == 0 or board[i + 1][j] == turn):
        return
    else:
        for k in range(i + 2, 8):
            if (board[k][j] == 0):
                return [k, j]
            elif (board[k][j] == turn):
                return
            else:
                continue
        return


def West(i, j, board, turn):
    if (board[i][j - 1] == 0 or board[i][j - 1] == turn):
        return
    else:
        for k in range(j - 2, -1, -1):
            if (board[i][k] == 0):
                return [i, k]
            elif (board[i][k] == turn):
                return
            else:
                continue
        return


def NorthEast(i, j, board, turn):
    if (board[i - 1][j + 1] == 0 or board[i - 1][j + 1] == turn):
        return
    else:
        for k1 in range(i - 2, -1, -1):
            for k2 in range(j + 2, 8):
                if (board[k1][k2] == 0):
                    return [k1, k2]
                elif (board[k1][k2] == turn):
                    return
                else:
                    continue
        return


def SouthEast(i, j, board, turn):
    if (board[i + 1][j + 1] == 0 or board[i + 1][j + 1] == turn):
        return
    else:
        for k1 in range(i + 2, 8):
            for k2 in range(j + 2, 8):
                if (board[k1][k2] == 0):
                    return [k1, k2]
                elif (board[k1][k2] == turn):
                    return
                else:
                    continue
        return


def SouthWest(i, j, board, turn):
    if (board[i + 1][j - 1] == 0 or board[i + 1][j - 1] == turn):
        return
    else:
        for k1 in range(i + 2, 8):
            for k2 in range(j - 2, -1, -1):
                if (board[k1][k2] == 0):
                    return [k1, k2]
                elif (board[k1][k2] == turn):
                    return
                else:
                    continue
        return


def NorthWest(i, j, board, turn):
    if (board[i - 1][j - 1] == 0 or board[i - 1][j - 1] == turn):
        return
    else:
        for k1 in range(i - 2, -1, -1):
            for k2 in range(j - 2, -1, -1):
                if (board[k1][k2] == 0):
                    return [k1, k2]
                elif (board[k1][k2] == turn):
                    return
                else:
                    continue
        return

def flipNorth(lists,board,i,j,turn):
	temp=copy.deepcopy(board)	
	for k in range(i-1,lists[0],-1):
		if turn==1:
			temp[k]j]=1
		else:
			temp[k][j]=-1
	return temp
			
def flipEast(lists,board,i,j,turn):
	temp=copy.deepcopy(board)	
	for k in range(j,lists[1]):
		if turn==1:
			temp[i]k]=1
		else:
			temp[i][k]=-1
	return temp
	
def flipSouth(lists,board,i,j,turn):
	temp=copy.deepcopy(board)	
	for k in range(i+1,lists[0]):
		if turn==1:
			temp[k]j]=1
		else:
			temp[k][j]=-1
	return temp

def flipWest(lists,board,i,j,turn):
	temp=copy.deepcopy(board)	
	for k in range(j-1,lists[1],-1):
		if turn==1:
			temp[i]k]=1
		else:
			temp[i][k]=-1
	return temp

def flipNorthEast(lists,board,i,j,turn):
	temp=copy.deepcopy(board)
	for k1 in range(i-1,lists[0],-1):
		for k2 in range(j+1,lists[1]):
			if turn==1:
				temp[k1]k2]=1
			else:
				temp[k1][k2]=-1
	return temp
				
def flipSouthEast(lists,board,i,j,turn):
	temp=copy.deepcopy(board)
	for k1 in range(i+1,lists[0]):
		for k2 in range(j+1,lists[1]):
			if turn==1:
				temp[k1]k2]=1
			else:
				temp[k1][k2]=-1
	return temp
				
def flipSouthWest(lists,board,i,j,turn):
	temp=copy.deepcopy(board)
	for k1 in range(i+1,lists[0]):
		for k2 in range(j-1,lists[1],-1):
			if turn==1:
				temp[k1]k2]=1
			else:
				temp[k1][k2]=-1
	return temp
				
def flipNorthWest(lists,board,i,j,turn):
	temp=copy.deepcopy(board)
	for k1 in range(i-1,lists[0],-1):
		for k2 in range(j-1,lists[1],-1):
			if turn==1:
				temp[k1]k2]=1
			else:
				temp[k1][k2]=-1		
	return temp		
		

def possibleAndFlip(board, i, j, turn):
    tbr = []
    states=[]
    tbr.append(North(i,j,board,turn))
    if tbr[-1]:
	newBoard=flipNorth(tbr[-1],board,i,j,turn)
	state=State(newBoard)
	states.append(state)
    tbr.append(East(i, j, board, turn))
    if tbr[-1]:
	newBoard=flipEast(tbr[-1],board,i,j,turn)
	state=State(newBoard)
	states.append(state)
    tbr.append(South(i, j, board, turn))
    if tbr[-1]:
	newBoard=flipSouth(tbr[-1],board,i,j,turn)
	state=State(newBoard)
	states.append(state)
    tbr.append(West(i, j, board, turn))
    if tbr[-1]:
	newBoard=flipWest(tbr[-1],board,i,j,turn)
	state=State(newBoard)
	states.append(state)
    tbr.append(NorthEast(i, j, board, turn))
    if tbr[-1]:
	newBoard=flipNorthEast(tbr[-1],board,i,j,turn)
	state=State(newBoard)
	states.append(state)
    tbr.append(SouthEast(i, j, board, turn))
    if tbr[-1]:
	newBoard=flipSouthEast(tbr[-1],board,i,j,turn)
	state=State(newBoard)
	states.append(state)
    tbr.append(SouthWest(i, j, board, turn))
    if tbr[-1]:
	newBoard=flipSouthWest(tbr[-1],board,i,j,turn)
	state=State(newBoard)
	states.append(state)
    tbr.append(NorthWest(i, j, board, turn))
    if tbr[-1]:
	newBoard=flipNorthWest(tbr[-1],board,i,j,turn)
	state=State(newBoard)
	states.append(state)
    return tbr,states

#def flip(board, possible_pos):
#    temp = copy.deepcopy(board)
#    temp.append(flipEast(board,i,j))
#    state = State(temp)


def Next(state, turn):
    state_array = []
    board = state.Board
    for i in range(0, 8):
        for j in range(0, 8):
            if (board[i][j] == turn):
                possible_pos,state_array = possibleAndFlip(board, i, j, turn)
                #new_states = flip(board, possible_pos)
                #np.concatenate(state_array, new_states)

    return state_array
