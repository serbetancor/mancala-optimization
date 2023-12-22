# File: rules.py

# Making a move function
def make_move(board, player, selected_hole, scores):
    # Check if it is valid
    if not (0 <= selected_hole <= 5):
        print("\nInvalid movement! Please choose between 1-6.")
        return "invalid movement"
    
    if  (board[player][selected_hole] == 0):
        print("\nInvalid movement! Please choose a hole with stones in it.")
        return "invalid movement"

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
                    scores[0] += 1
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
                    scores[1] += 1
                    stones -= 1
                if stones > 0:
                    current_hole = 0
                direction = 1 - direction

            else:
                board[direction][current_hole] += 1
                stones -= 1
                current_hole -= 1

    current_hole = current_hole + 1 if direction == 0 else current_hole - 1
    
    if board[direction][current_hole] == 1 and direction==player and board[1- direction][current_hole] != 0:
        scores[1 - direction] += board[1 - direction][current_hole] + 1
        board[direction][current_hole] = 0
        board[1 - direction][current_hole] = 0

# Función para verificar el estado del juego
def verificar_estado_juego(board):
    # Si alguno de los lados está vacío, el juego ha terminado
    if sum(board[0]) == 0 or sum(board[1]) == 0:
        # Capturar las semillas restantes y agregarlas a los mancalas
        board[0][6] += sum(board[0])
        board[1][6] += sum(board[1])
        # Determinar al ganador
        if board[0][6] > board[1][6]:
            return "¡Jugador 1 gana!"
        elif board[0][6] < board[1][6]:
            return "¡Jugador 2 gana!"
        else:
            return "¡Es un empate!"
    else:
        return "El juego aún no ha terminado."