import tkinter as tk
from rules import make_move, game_status

class MancalaUI:
    def __init__(self, root, board, scores, players):
        self.root = root
        self.root.title("Mancala Game")

        self.board = board
        self.scores = scores
        self.players = players
        self.current_player = 1

        self.label_board = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_scores = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_turn = tk.Label(root, text="", font=("Helvetica", 14, "bold"))

        self.entry_hole = tk.Entry(root, width=5)
        self.btn_make_move = tk.Button(root, text="Make Move", command=self.make_move)

        self.label_board.pack()
        self.label_scores.pack()
        self.label_turn.pack()

        tk.Label(root, text="Select hole (1-6):").pack()
        self.entry_hole.pack()
        self.btn_make_move.pack()

        self.update_display()

    def make_move(self):
        selected_hole = int(self.entry_hole.get())
        result = make_move(self.board, self.current_player, selected_hole - 1, self.scores)
        if result != "error":
            self.update_display()
            game_state = game_status(self.board, self.scores, self.players)

            if "wins" in game_state.lower() or "tie" in game_state.lower():
                tk.messagebox.showinfo("Game Over", game_state)
                self.root.destroy()
                return

            self.current_player = result

    def update_display(self):
        board_str = f"\n   {self.board[0]}\n{self.scores[0]}                      {self.scores[1]}\n   {self.board[1]}"
        self.label_board.config(text=board_str)

        scores_str = f"{self.players[0]}: {self.scores[0]}  |  {self.players[1]}: {self.scores[1]}"
        self.label_scores.config(text=scores_str)

        turn_str = f"{self.players[self.current_player - 1]}'s turn"
        self.label_turn.config(text=turn_str)

def run_ui(board, scores, players):
    root = tk.Tk()
    mancala_ui = MancalaUI(root, board, scores, players)
    root.mainloop()

if __name__ == "__main__":
    # Copia tu código existente aquí para inicializar el juego
    board = [
        [4, 4, 4, 4, 4, 4],  # Player 2
        [4, 4, 4, 4, 4, 4],  # Player 1
    ]
    players = ["Nuria", "Sergio"]
    scores = [0, 0]
    
    run_ui(board, scores, players)
