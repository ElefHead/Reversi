from os import listdir
from os import path
from pprint import pprint
import numpy as np 

input_dir = "input"
output_dir = "output"

weights = np.array([[99,-8,8,6,6,8,-8,99],
					[-8,-24,-4,-3,-3,-4,-24,-8],
					[8,-4,7,4,4,7,-4,8],
					[6,-3,4,0,0,4,-3,6],
					[6,-3,4,0,0,4,-3,6],
					[8,-4,7,4,4,7,-4,8],
					[-8,-24,-4,-3,-3,-4,-24,-8],
					[99,-8,8,6,6,8,-8,99]])

naming = {
	'X':2,
	'O':1,
	'*':0,
	0:"a",
	1:"b",
	2:"c",
	3:"d",
	4:"e",
	5:"f",
	6:"g",
	7:"h"
}

global passes
global best_move


def getWeightSum(board,player):
	if player=='X':
		board[board==naming['O']] = 0
		board[board==naming['X']] = 1
	else:
		board[board==naming['X']] = 0
		board[board==naming['O']] = 1
	return int(np.sum(np.multiply(weights,board)))

def evaluate(board):
	return getWeightSum(np.array(board),"X") - getWeightSum(np.array(board),"O")

def getValidMoves(board,player):
	valid_moves = []
	for i in range(len(board)):
		for j in range(len(board)):
			if isValidMove(np.array(board),(i,j),player):
				valid_moves.append((i,j))
	return valid_moves

def hasVerticalUpwards(board,position,tile): #Walk upwards from empty space till you keep encountering opponent tiles. Return true if tile
	opponent_tile = 1 if tile==2 else 2		 #you land on is player tile. Return false in all other cases.
	found_opponent = False
	for i in range(position[0]-1,-1,-1):
		if board[i][position[1]] == opponent_tile:
			found_opponent = True
		else:
			break
	if found_opponent and i>=0:
		if board[i][position[1]] == tile:
			return True
	return False

def hasVerticalDownwards(board,position,tile):
	opponent_tile = 1 if tile==2 else 2
	found_opponent = False
	for i in range(position[0]+1,8,1):
		if board[i][position[1]] == opponent_tile:
			found_opponent = True
		else:
			break
	if found_opponent and i<8:
		if board[i][position[1]] == tile:
			return True
	return False

def hasHorizontalLeft(board,position,tile):
	opponent_tile = 1 if tile==2 else 2
	found_opponent = False
	for j in range(position[1]-1,-1,-1):
		if board[position[0]][j] == opponent_tile:
			found_opponent = True
		else:
			break
	if found_opponent and j>=0:
		if board[position[0]][j] == tile:
			return True
	return False

def hasHorizontalRight(board,position,tile):
	opponent_tile = 1 if tile==2 else 2
	found_opponent = False
	for j in range(position[1]+1,8,1):
		if board[position[0]][j] == opponent_tile:
			found_opponent = True
		else:
			break
	if found_opponent and j<8:
		if board[position[0]][j] == tile:
			return True
	return False

def hasDiagonalUpLeft(board,position,tile):
	opponent_tile = 1 if tile==2 else 2
	found_opponent = False
	i,j = position[0]-1,position[1]-1
	while(i>=0 and j>=0):
		if board[i][j] == opponent_tile:
			found_opponent = True
			i,j = i-1,j-1
		else:
			break
	if found_opponent and i>=0 and j>=0:
		if board[i][j] == tile:
			return True
	return False

def hasDiagonalUpRight(board,position,tile):
	opponent_tile = 1 if tile==2 else 2
	found_opponent = False
	i,j = position[0]-1,position[1]+1
	while(i>=0 and j<8):
		if board[i][j] == opponent_tile:
			found_opponent = True
			i,j = i-1,j+1
		else:
			break
	if found_opponent and i>=0 and j<8:
		if board[i][j] == tile:
			return True
	return False

def hasDiagonalDownRight(board,position,tile):
	opponent_tile = 1 if tile==2 else 2
	found_opponent = False
	i,j = position[0]+1,position[1]+1
	while(i<8 and j<8):
		if board[i][j] == opponent_tile:
			found_opponent = True
			i,j = i+1,j+1
		else:
			break
	if found_opponent and i<8 and j<8:
		if board[i][j] == tile:
			return True
	return False

def hasDiagonalDownLeft(board,position,tile):
	opponent_tile = 1 if tile==2 else 2
	found_opponent = False
	i,j = position[0]+1,position[1]-1
	while(i<8 and j>=0):
		if board[i][j] == opponent_tile:
			found_opponent = True
			i,j = i+1,j-1
		else:
			break
	if found_opponent and i<8 and j>=0:
		if board[i][j] == tile:
			return True
	return False

def isValidMove(board,position,player):
	if board[position[0]][position[1]] != 0:
		return False
	tile = naming[player]
	if hasVerticalUpwards(board,position,tile):
		return True
	if hasVerticalDownwards(board,position,tile):
		return True
	if hasHorizontalLeft(board,position,tile):
		return True
	if hasHorizontalRight(board,position,tile):
		return True
	if hasDiagonalUpRight(board,position,tile):
		return True
	if hasDiagonalUpLeft(board,position,tile):
		return True
	if hasDiagonalDownRight(board,position,tile):
		return True
	if hasDiagonalDownLeft(board,position,tile):
		return True 
	return False

def moveVerticalUpwards(board, position, tile):
	opponent_tile = 1 if tile == 2 else 2
	for i in range(position[0]-1,-1,-1):
		if board[i][position[1]] == opponent_tile:
			board[i][position[1]] = tile
		else:
			break
	return board

def moveVerticalDownwards(board, position, tile):
	opponent_tile = 1 if tile == 2 else 2
	for i in range(position[0]+1,8):
		if board[i][position[1]] == opponent_tile:
			board[i][position[1]] = tile
		else:
			break
	return board

def moveHorizontalLeft(board, position, tile):
	opponent_tile = 1 if tile == 2 else 2
	for j in range(position[1]-1,-1,-1):
		if board[position[0]][j] == opponent_tile:
			board[position[0]][j] = tile
		else:
			break
	return board

def moveHorizontalRight(board, position, tile):
	opponent_tile = 1 if tile == 2 else 2
	for j in range(position[1]+1,8):
		if board[position[0]][j] == opponent_tile:
			board[position[0]][j] = tile
		else:
			break
	return board

def moveDiagonalUpLeft(board, position, tile):
	opponent_tile = 1 if tile == 2 else 2
	i,j = position[0]-1,position[1]-1
	while(i>=0 and j>=0):
		if board[i][j] == opponent_tile:
			board[i][j] = tile
			i,j = i-1,j-1
		else:
			break
	return board

def moveDiagonalUpRight(board, position, tile):
	opponent_tile = 1 if tile == 2 else 2
	i,j = position[0]-1,position[1]+1
	while(i>0 and j<8):
		if board[i][j] == opponent_tile:
			board[i][j] = tile
			i,j = i-1,j+1
		else:
			break
	return board

def moveDiagonalDownRight(board, position, tile):
	opponent_tile = 1 if tile == 2 else 2
	i,j = position[0]+1,position[1]+1
	while(i<8 and j<8):
		if board[i][j] == opponent_tile:
			board[i][j] = tile
			i,j = i+1,j+1
		else:
			break
	return board

def moveDiagonalDownLeft(board, position, tile):
	opponent_tile = 1 if tile == 2 else 2
	i,j = position[0]+1,position[1]-1
	while(i<8 and j>=0):
		if board[i][j] == opponent_tile:
			board[i][j] = tile
			i,j = i+1,j-1
		else:
			break
	return board

def makeMove(board, position, player):
	currentState = np.array(board)
	tile = naming[player]
	if position == "pass":
		return board
	if hasVerticalUpwards(board, position, tile):
		board = moveVerticalUpwards(board,position,tile)
	if hasVerticalDownwards(board, position, tile):
		board = moveVerticalDownwards(board, position, tile)
	if hasHorizontalLeft(board, position, tile):
		board = moveHorizontalLeft(board, position, tile)
	if hasHorizontalRight(board, position, tile):
		board = moveHorizontalRight(board, position, tile)
	if hasDiagonalUpLeft(board, position, tile):
		board = moveDiagonalUpLeft(board, position, tile)
	if hasDiagonalUpRight(board, position, tile):
		board = moveDiagonalUpRight(board, position, tile)
	if hasDiagonalDownLeft(board, position, tile):
		board = moveDiagonalDownLeft(board, position, tile)
	if hasDiagonalDownRight(board, position, tile):
		board = moveDiagonalDownRight(board, position, tile)
	if(not np.array_equal(currentState,board)):
		board[position[0]][position[1]] = tile
	return board

def genLog(depth,chosen_score,chosen_move,alpha,beta):
	log = ""
	if(depth == 0):
		log = log+"root,"
	elif(chosen_move=="pass"):
		log = log+"pass,"
	else:
		log = log+naming[chosen_move[1]]+str(chosen_move[0]+1)+","
	log = log+str(depth)+","
	if chosen_score == -1*float("inf"):
		log = log+"-Infinity,"
	elif chosen_score == float("inf"):
		log = log+"Infinity,"
	else:
		log=log+str(chosen_score)+","
	log = log+"-Infinity," if alpha==-1*float("inf") else log+str(alpha)+","
	log = log+"Infinity" if beta==float("inf") else log+str(beta)
	return log

def alphabeta(board, depth, max_depth, alpha, beta, player, is_max, mov): #Mov is the node
	global best_move
	global passes
	opponent = "O" if player=="X" else "X"
	if depth == max_depth or passes==2:
		value = evaluate(board)
		return value
	if is_max:
		value = -1*float("inf")
		moves = getValidMoves(board,player)
		if moves==[]:
			passes = passes+1
			value = max(value,alphabeta(makeMove(np.array(board),"pass",player), depth+1, max_depth,alpha,beta,opponent,False,"pass"))
			if value>alpha:
				alpha = value
		else:
			for move in moves:
				value = max(value,alphabeta(makeMove(np.array(board),move,player), depth+1, max_depth, alpha, beta, opponent, False, move))
				if value>alpha:
					alpha = value
					best_move = move
				else:
					alpha = alpha
					
				if beta<=alpha:
					break
	else:
		value = float('inf')
		moves = getValidMoves(board,player)		
		if moves == []:
			passes = passes + 1
			value = min(value,alphabeta(makeMove(np.array(board),"pass",player),depth+1,max_depth,alpha,beta,opponent,True,"pass"))
			if value<beta:
				beta = value
		else:			
			for move in moves:
				value = min(value,alphabeta(makeMove(np.array(board),move,player), depth+1, max_depth, alpha, beta,opponent,True, move))
				beta = min(beta,value)
				if beta<=alpha:
					break
	return value

def main():
	for f in listdir(input_dir):
		board = []
		global passes
		global best_move
		passes = 0
		best_move = ()
		if ".txt" in f:
			with open(path.join(".",input_dir,f),"r") as r:
				player = r.readline().strip()
				depth = int(r.readline().strip())
				for line in r.read().split("\n"):
					board.append(list(line.strip().replace("*","0").replace("O","1").replace("X","2")))
				board = np.asarray(board,dtype="int")
				score = alphabeta(board,0,depth,-1*float("inf"),float("inf"),player,True,None)
				pprint((score,best_move))


if __name__ == '__main__':
	main()