import tkinter as tk

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DSP332 - Practical Assignment - Team 13")

        # Créer un canvas
        self.canvas = tk.Canvas(master)
        self.canvas.pack(side="top", fill="both", expand=True)

        # Afficher le humanUserLogo
        self.humanUserLogo = tk.PhotoImage(file="humanUserLogo.png")
        self.humanUserLogo = self.humanUserLogo.subsample(10, 10)
        self.humanUserLabel = tk.Label(self.canvas, image=self.humanUserLogo)
        self.humanUserLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.human_player_label = tk.Label(self.canvas, text="Human Player\nScore: 0")
        self.human_player_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        # Afficher le computerPlayerLogo
        self.computerPlayerLogo = tk.PhotoImage(file="computerPlayerLogo.png")
        self.computerPlayerLogo = self.computerPlayerLogo.subsample(10, 10)
        self.computerPlayerLabel = tk.Label(self.canvas, image=self.computerPlayerLogo)
        self.computerPlayerLabel.grid(row=0, column=6, sticky="w", padx=10, pady=10)

        self.computer_player_label = tk.Label(self.canvas, text="Computer Player\nScore: 0")
        self.computer_player_label.grid(row=0, column=5, sticky="e", padx=10, pady=10)

        # Afficher le vsLogo
        self.vsLogo = tk.PhotoImage(file="vsLogo.png")
        self.vsLogo = self.vsLogo.subsample(10, 10)
        self.vsLabel = tk.Label(self.canvas, image=self.vsLogo)
        self.vsLabel.grid(row=0, column=3, padx=10, pady=10)

    def update_scores(self, human_score, computer_score):
        self.human_player_label.config(text=f"Human Player\nScore: {human_score}")
        self.computer_player_label.config(text=f"Computer Player\nScore: {computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)

    # Exemple de mise à jour des scores
    game_gui.update_scores(5, 10)

    root.mainloop()
