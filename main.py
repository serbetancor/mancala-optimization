# Archivo: main.py
from mancala.board import print_board
from mancala.rules import make_move, game_status

def main():
    # Initial representation
    # board = [
    #     [4, 4, 4, 4, 4, 4],  # Player 2
    #     [4, 4, 4, 4, 4, 4],  # Player 1
    # ]

    board = [
        [1, 0, 0, 0, 0, 0],  # Player 2
        [0, 0, 0, 0, 0, 1],  # Player 1
    ]

    players = ["Nuria", "Sergio"]
    player = 1
    scores = [0, 0]

    print_board(board, scores, players)

    while True:
        selected_hole = int(input(f"\n<---------------------------------->\n\nTurno de {players[player]}. Elige un hoyo (1-6): "))
        result = make_move(board, player, selected_hole - 1, scores)
        if result != "error":
            game_state = game_status(board, scores, players)
            print_board(board, scores, players)

            if "wins" in game_state.lower() or "tie" in game_state.lower():
                print("\n<---------------------------------->\n\n", game_state)
                break



            player = result  # Alternate between players

if __name__ == "__main__":
    main()
