# Archivo: main.py
from mancala.board import print_board
from mancala.rules import make_move, verificar_estado_juego

def main():
    # Initial representation
    board = [
        [4, 4, 4, 4, 4, 4],  # Player 2
        [4, 4, 4, 4, 4, 4],  # Player 1
    ]

    player = 1
    scores = [0, 0]

    print_board(board, scores)

    while True:
        selected_hole = int(input(f"\n<---------------------------------->\n\nTurno del Jugador {player}. Elige un hoyo (1-6): "))
        if not make_move(board, player, selected_hole - 1, scores) == "invalid movement":
            print_board(board, scores)
            game_state = verificar_estado_juego(board)

            if "gana" in game_state.lower() or "empate" in game_state.lower():
                print(game_state)
                break

            player = 1- player  # Alternate between players

if __name__ == "__main__":
    main()
