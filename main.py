# Archivo: main.py
from mancala.board import print_board
from mancala.logic import make_move, game_status
from mancala.minimax import find_best_move

def main():
    # Initial representation
    board = [
        [0, 3, 2, 5, 2, 5],  # Player
        [6, 3, 6, 3, 3, 5]  # Bot
    ]

    players = ["Pablo", "Sergio"]
    player = 1
    scores = [1, 0]

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

if __name__ == "__main__":
    main()
