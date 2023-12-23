# File: minimax.py

from mancala.logic import make_move

def evaluate_board(player, scores):
    # Esta es una función de evaluación simple que resta los puntajes del oponente
    # de los puntajes del jugador actual.
    return scores[player] - scores[1 - player]

def minimax(board, depth, maximizing_player, player, scores):
    if depth == 0 or sum(board[0]) == 0 or sum(board[1]) == 0:
        return evaluate_board(player, scores)

    if maximizing_player:
        max_eval = float('-inf')
        for move in range(6):
            if board[player][move] != 0:
                new_board = [row[:] for row in board]
                new_scores = scores[:]
                new_player = make_move(new_board, player, move, new_scores)
                eval = minimax(new_board, depth - 1, True, new_player, new_scores)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in range(6):
            if board[player][move] != 0:
                new_board = [row[:] for row in board]
                new_scores = scores[:]
                new_player = make_move(new_board, player, move, new_scores)
                eval = minimax(new_board, depth - 1, False, new_player, new_scores)
                min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board, player, scores):
    best_move = -1
    best_eval = float('-inf')

    for move in range(6):
        if board[player][move] != 0:
            new_board = [row[:] for row in board]
            new_scores = scores[:]
            new_player = make_move(new_board, player, move, new_scores)
            eval = minimax(new_board, 5, False, new_player, new_scores)  # Puedes ajustar la profundidad
            if eval > best_eval:
                best_eval = eval
                best_move = move

    print("\nSergio should play ", best_move + 1, ".\n")
    return best_move

