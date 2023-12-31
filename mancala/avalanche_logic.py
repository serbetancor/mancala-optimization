# File: avalanche_logic.py

import time

# Making a move function
def move_avalanche(board, player, selected_hole, scores):
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
                    stones = check_last_stone(board, current_hole, direction, stones)

                if stones > 0:
                    current_hole = 5 
                direction =  1 - direction
                
            else:
                board[direction][current_hole] += 1
                stones -= 1
                stones = check_last_stone(board, current_hole, direction, stones)

                current_hole += 1

        else:
            if current_hole < 0:
                if direction == player:
                    scores[0] += 1
                    stones -= 1
                    stones = check_last_stone(board, current_hole, direction, stones)
                if stones > 0:
                    current_hole = 0
                direction = 1 - direction

            else:
                board[direction][current_hole] += 1
                stones -= 1
                stones = check_last_stone(board, current_hole, direction, stones)
                current_hole -= 1

    current_hole = current_hole + 1 if direction == 0 else current_hole - 1
    return player if (current_hole == 7 or current_hole == -2) else 1 - player

def check_last_stone(board, current_hole, direction, stones):
    if stones == 0 and -1 < current_hole < 6 and board[direction][current_hole] != 1:
        stones = board[direction][current_hole]
        board[direction][current_hole] = 0

    return stones