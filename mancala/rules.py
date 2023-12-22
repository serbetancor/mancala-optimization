# Optimiza este código de Python al máximo. Recuerda conservar todas las funcionalidades lógicas. Quiero que mi resultado sea exactamente igual. Respira y no cometas errores.

# File: rules.py

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
        scores[direction] += board[direction][current_hole] + 1
        board[direction][current_hole] = 0
        board[1 - direction][current_hole] = 0 

    return player if (current_hole == 7 or current_hole == -2) else 1 - player

# Checking game state
def game_status(board, scores, players):

    if sum(board[0]) == 0 or sum(board[1]) == 0:

        scores[0] += sum(board[0])
        scores[1] += sum(board[1])

        board[0] = board[1] = [0] * 6

        if scores[1] > scores[0]:
            return f"{players[1]} wins!"
        elif scores[0] > scores[1]:
            return f"{players[0]} wins!"
        else:
            return f"It's a tie between {players[1]} and {players[0]}!\n"
    else:
        return "Game still in progress."