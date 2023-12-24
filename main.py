# Archivo: main.py
from mancala.capture_logic import start_capture
from mancala.avalanche_logic import start_avalanche

def main():
    # Initial representation
    board = [
        [4, 4, 4, 4, 4, 4],  # Player
        [4, 4, 4, 4, 4, 4]  # Bot
    ]

    players = ["Pablo", "Sergio"]
    player = 1
    scores = [0, 0]

    mode_select = int(input(f"\n<---------------------------------->What game mode do you want to play?:\n1) Capture\n2) Avalanche"))
    if mode_select == 1:
        start_capture(board, players, player, scores)
    elif mode_select == 2:
        start_avalanche(board, players, player, scores)
    else:
        print("Please enter a valid game mode.")


if __name__ == "__main__":
    main()
