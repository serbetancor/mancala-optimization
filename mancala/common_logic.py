# File: common_logic.py

# Checking game state
def game_status(board, scores, players):

    if sum(board[0]) == 0 or sum(board[1]) == 0:
        if scores[1] > scores[0]:
            return f"{players[1]} wins!"
        elif scores[0] > scores[1]:
            return f"{players[0]} wins!"
        else:
            return f"It's a tie between {players[1]} and {players[0]}!\n"
    else:
        return "Game still in progress."