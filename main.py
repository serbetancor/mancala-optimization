# Archivo: main.py
from mancala.run_start import start_capture
from mancala.run_start import start_avalanche

def main():
    # Initial representation
    board = [
        [4, 4, 4, 4, 4, 4],  # Player
        [4, 4, 4, 4, 4, 4]  # Bot
    ]

    players = ["Pablo", "Sergio"]
    player = 0
    scores = [0, 0]

    mode_select = int(input(f"\nWhat game mode do you want to play?:\n1) Capture\n2) Avalanche\n\nSelect game mode -> "))
    if mode_select == 1:
        start_capture(board, players, player, scores)
    elif mode_select == 2:
        start_avalanche(board, players, player, scores)
    else:
        print("Please enter a valid game mode.")


if __name__ == "__main__":
    main()
