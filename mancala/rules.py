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
                direction =  1 - direction
                current_hole = 5
                scores[0] += 1
                stones -= 1
            else:
                board[direction][current_hole] += 1
                stones -= 1
                current_hole += 1

        else:
            if current_hole < 0:
                direction = 1 - direction
                current_hole = 0
                scores[1] += 1
                stones -= 1
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
def verificar_estado_juego(tablero):
    # Si alguno de los lados está vacío, el juego ha terminado
    if sum(tablero[0]) == 0 or sum(tablero[1]) == 0:
        # Capturar las semillas restantes y agregarlas a los mancalas
        tablero[0][6] += sum(tablero[0])
        tablero[1][6] += sum(tablero[1])
        # Determinar al ganador
        if tablero[0][6] > tablero[1][6]:
            return "¡Jugador 1 gana!"
        elif tablero[0][6] < tablero[1][6]:
            return "¡Jugador 2 gana!"
        else:
            return "¡Es un empate!"
    else:
        return "El juego aún no ha terminado."