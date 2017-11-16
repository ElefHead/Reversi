best_move = None

def alphabeta(board, depth, max_depth, alpha, beta, player, is_max, move): #Move is the node
	opponent = "O" if player=="X" else "X"
	if depth == max_depth or passes==2:
		value = evaluate(board)
		return value
	if is_max:
		value = -1*float("inf")
		moves = getValidMoves(board,player)
		if moves==[]:
			passes = passes+1
			score = alphabeta(makeMove(np.array(board),"pass",player), depth+1, max_depth,alpha,beta,opponent,False,"pass")
		else:
			for move in moves:
				value = alphabeta(makeMove(np.array(board),move,player), depth+1, max_depth, alpha, beta, False, move)
				if value>alpha:
					alpha = value
					best_move = move
				if beta<=alpha:
					break
	else:
		value = float('inf')
		moves = getValidMoves(board,player)
		if moves == []:
			passes = passes + 1
			score = alphabeta(makeMove(np.array(board),"pass",player),depth+1,max_depth,alpha,beta,opponent,True,"pass")
		else:
			for move in moves:
				value = alphabeta(makeMove(np.array(board),move,player), depth+1, max_depth, alpha, beta, True, move)
				if value < beta:
					beta = value
				if beta<=alpha:
					break
	return value
