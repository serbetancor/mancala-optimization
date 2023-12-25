# File: minimax.py

from mancala.capture_logic import move_capture
from mancala.avalanche_logic import move_avalanche
from mancala.common_logic import game_status

def minimax(board, depth, maximizing_player, alpha, beta, player, players, scores, mode):
    if depth == 0 or game_status(board, scores, players) != "Game still in progress.":
        return scores[1] - scores[0]

    legal_moves = [i for i in range(6) if board[player][i] > 0]
    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            new_board = [row[:] for row in board]
            new_scores = scores[:]
            result = move_capture(new_board, player, move, new_scores) if mode == "capture" else move_avalanche(new_board, player, move, new_scores)
            if result != player:
                eval = minimax(new_board, depth - 1, False, alpha, beta, 1 - player, players, new_scores, mode)
            else:
                eval = minimax(new_board, depth, True, alpha, beta, player, players, new_scores, mode)

            max_eval = max(max_eval, eval)
            alpha = max(alpha, max_eval)
            if max_eval >= beta:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            new_board = [row[:] for row in board]
            new_scores = scores[:]
            result = move_capture(new_board, player, move, new_scores) if mode == "capture" else move_avalanche(new_board, player, move, new_scores)
            if result != player:
                eval = minimax(new_board, depth - 1, True, alpha, beta, 1 - player, players, new_scores, mode)
            else:
                eval = minimax(new_board, depth, False, alpha, beta, player, players, new_scores, mode)
            
            min_eval = min(min_eval, eval)
            beta = min(beta, min_eval)
            if min_eval <= alpha:
                break
        return min_eval

def find_best_move(board, player, players, scores, mode):
    best_score = float('-inf')
    best_move = -1
    alpha = float('-inf')
    beta = float('inf')
    depth = 5 if mode == "avalanche" else 10

    legal_moves = [i for i in range(6) if board[player][i] > 0]

    for move in legal_moves:
        new_board = [row[:] for row in board]
        new_scores = scores[:]
        result = move_capture(new_board, player, move, new_scores) if mode == "capture" else move_avalanche(new_board, player, move, new_scores)

        if result != player:
            eval = minimax(new_board, depth, False, alpha, beta, 1 - player, players, new_scores, mode)
        else:
            eval = minimax(new_board, depth + 1, True, alpha, beta, player, players, new_scores, mode)

        if eval > best_score:
            best_score = eval
            best_move = move

    print(f"\n{players[player]} decides to play {best_move + 1}.\nBest score -> {best_score}")
    return best_move
