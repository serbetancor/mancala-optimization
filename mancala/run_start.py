# File: run_start.py

from mancala.board import print_board
from mancala.minimax import find_best_move
from mancala.capture_logic import make_move
from mancala.common_logic import game_status

def start_capture(board, players, player, scores):
    print_board(board, scores, players)

    while True:
        # selected_hole = find_best_move(board, player, players, scores) 

        if player == 1:
            selected_hole = find_best_move(board, player, players, scores)
        else:
            selected_hole = int(input(f"\n<---------------------------------->\n\n{players[player]}'s turn. Choose a position (1-6): ")) - 1
            
        result = make_move(board, player, selected_hole, scores)
        if result != "error":
            game_state = game_status(board, scores, players)
            print_board(board, scores, players)

            if "wins" in game_state.lower() or "tie" in game_state.lower():
                print("\n<---------------------------------->\n\n", game_state)
                break
            
            player = result  # Alternate between players

def start_avalanche(board, players, player, scores):
    print("Avalanche logic in progress...\n")