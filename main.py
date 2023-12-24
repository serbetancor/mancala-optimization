import tkinter as tk

def start_game(mode):
    print(f"Starting the game with {mode} mode.")

def choose_mode():
    root = tk.Tk()
    root.title("Mancala Game - Mode Selection")
    root.geometry("650x1000")

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True, fill=tk.BOTH)  # Ocupa todo el espacio

    # Botón para el modo "Capture"
    capture_button = tk.Button(button_frame, text="Capture", command=lambda: start_game("Capture"))
    capture_button.pack(expand=True, fill=tk.BOTH, padx=25, pady=25)  # Ocupa todo el espacio dentro del Frame

    # Botón para el modo "Avalanche"
    avalanche_button = tk.Button(button_frame, text="Avalanche", command=lambda: start_game("Avalanche"))
    avalanche_button.pack(expand=True, fill=tk.BOTH, padx=25, pady=25)  # Ocupa todo el espacio disponible

    root.mainloop()

def main():
    choose_mode()

if __name__ == "__main__":
    main()
