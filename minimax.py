# def minimax(board, depth, max_depth, alpha, beta, player, chosen_score, chosen_move):
# 	opponent = "O" if player == "X" else "X"
# 	if depth == max_depth:
# 		print "In leaf"
# 		chosen_score = evaluate(board)
# 	else:
# 		print "Not Leaf"
# 		moves = getValidMoves(board,player)
# 		pprint(moves)
# 		if moves == []:
# 			chosen_score = evaluate(board)
# 		else:
# 			best_score = -1*float("inf")
# 			best_move = ()
# 			for move in moves:
# 				the_score,the_move = minimax(makeMove(np.array(board),move,player),depth+1,max_depth,opponent,chosen_score,move)
# 				if the_score >= best_score:
# 					best_score,best_move = the_score,the_move
# 			chosen_score, chosen_move = best_score, best_move
# 	return (chosen_score, chosen_move)