# File: minimax.py

from board import print_board
from rules import make_move, game_status

def evaluate_board(board, player, scores):
    # Esta es una función de evaluación simple que resta los puntajes del oponente
    # de los puntajes del jugador actual.
    return scores[player] - scores[1 - player]

def minimax(board, depth, maximizing_player, player, scores):
    if depth == 0 or sum(board[0]) == 0 or sum(board[1]) == 0:
        return evaluate_board(board, player, scores)

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

# Puedes agregar esta función en tu archivo main.py para que la IA juegue automáticamente.
def play_with_minimax():
    # Initial representation
    board = [
        [3, 5, 4, 5, 2, 3],  # Player 2
        [3, 2, 5, 4, 5, 3],  # Player 1
    ]

    players = ["Pablo", "Sergio"]
    player = 0
    scores = [0, 0]

    print_board(board, scores, players)

    while True:
        if player == 1:
            selected_hole = find_best_move(board, player, scores) + 1
        else:
            selected_hole = int(input(f"\n<---------------------------------->\n\n{players[player]}'s turn. Choose a position (1-6): "))
            
        result = make_move(board, player, selected_hole - 1, scores)
        if result != "error":
            game_state = game_status(board, scores, players)
            print_board(board, scores, players)

            if "wins" in game_state.lower() or "tie" in game_state.lower():
                print("\n<---------------------------------->\n\n", game_state)
                break
            
            player = result  # Alternate between players

if __name__ == "__main__":
    play_with_minimax()
