# File: minimax.py

from mancala.logic import make_move, game_status

def minimax(board, depth, maximizing_player, alpha, beta, player, players, scores):
    if depth == 0 or game_status(board, scores, players) != "Game still in progress.":
        return scores[player] - scores[1 - player]

    legal_moves = [i for i in range(6) if board[player][i] > 0]
    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            new_board = [row[:] for row in board]
            new_scores = scores[:]
            result = make_move(new_board, player, move, new_scores)
            if result != "error":
                if result != player:
                    eval = minimax(new_board, depth - 1, False, alpha, beta, 1 - player, players, new_scores)
                else:
                    eval = minimax(new_board, depth - 1, True, alpha, beta, player, players, new_scores)

                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            new_board = [row[:] for row in board]
            new_scores = scores[:]
            result = make_move(new_board, player, move, new_scores)
            if result != "error":
                if result != player:
                    eval = minimax(new_board, depth - 1, True, alpha, beta, 1 - player, players, new_scores)
                else:
                    eval = minimax(new_board, depth - 1, False, alpha, beta, player, players, new_scores)
                
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board, player, players, scores):
    best_score = float('-inf')
    best_move = -1
    alpha = float('-inf')
    beta = float('inf')

    legal_moves = [i for i in range(6) if board[player][i] > 0]

    for move in legal_moves:
        new_board = [row[:] for row in board]
        new_scores = scores[:]
        result = make_move(new_board, player, move, new_scores)
        if result != "error":
            if result != player:
                eval = minimax(new_board, 12, False, alpha, beta, 1 - player, players, new_scores)
            else:
                eval = minimax(new_board, 12, True, alpha, beta, player, players, new_scores)

            if eval > best_score:
                best_score = eval
                best_move = move

    print(f"\n{players[player]} decides to play {best_move + 1}.\n")
    return best_move
