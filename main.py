# Archivo: main.py
from mancala.run_start import run_start

def main():
    # Initial representation
    board = [
        [4, 4, 2, 4, 1, 2],  # Player
        [2, 1, 1, 2, 4, 4]  # Bot
    ]

    players = ["Sergio", "Nuria"]
    player = 0
    scores = [0, 0]

    while True:
        mode_select = int(input(f"\nWhat game mode do you want to play?:\n1) Capture\n2) Avalanche\n\nSelect game mode -> "))
        if mode_select == 1:
            run_start(board, players, player, scores, "capture")
        elif mode_select == 2:
            run_start(board, players, player, scores, "avalanche")
        else:
            print("Please enter a valid game mode.")


if __name__ == "__main__":
    main()
