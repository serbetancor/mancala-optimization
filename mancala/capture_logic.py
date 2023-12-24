# File: capture_logic.py

from board import print_board
from minimax import find_best_move
from common_logic import game_status

# Making a move function
def make_move(board, player, selected_hole, scores):
    # Check if it is valid
    if not (0 <= selected_hole <= 5):
        print("\nInvalid movement! Please choose between 1-6.")
        return "error"
    
    if  (board[player][selected_hole] == 0):
        print("\nInvalid movement! Please choose a hole with stones in it.")
        return "error"

    stones = board[player][selected_hole]
    board[player][selected_hole] = 0

    direction = player

    # Distribute all stones
    current_hole = selected_hole + (1 if direction == 1 else -1)
    while stones > 0:
        if direction == 1:
            # Change board side
            if current_hole > 5:
                if direction == player:
                    scores[1] += 1
                    stones -= 1
                if stones > 0:
                    current_hole = 5 
                direction =  1 - direction
                
            else:
                board[direction][current_hole] += 1
                stones -= 1
                current_hole += 1

        else:
            if current_hole < 0:
                if direction == player:
                    scores[0] += 1
                    stones -= 1
                if stones > 0:
                    current_hole = 0
                direction = 1 - direction

            else:
                board[direction][current_hole] += 1
                stones -= 1
                current_hole -= 1
    
    current_hole = current_hole + 1 if direction == 0 else current_hole - 1
    if (6 > current_hole > -1) and board[direction][current_hole] == 1 and direction==player and board[1- direction][current_hole] != 0:
        scores[direction] += board[1 -direction][current_hole] + 1
        board[direction][current_hole] = 0
        board[1 - direction][current_hole] = 0 

    if sum(board[0]) == 0 or sum(board[1]) == 0:
        scores[0] += sum(board[0])
        scores[1] += sum(board[1])
        board[0] = board[1] = [0] * 6

    return player if (current_hole == 7 or current_hole == -2) else 1 - player

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