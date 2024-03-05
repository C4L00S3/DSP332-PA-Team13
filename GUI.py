import tkinter as tk
#liste de taille aléatoire entre 15 et 25 contenant des entiers aléatoires entre 1 et 9
import random
liste = [random.randint(1, 9) for i in range(random.randint(15, 25))]
class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DSP332 - Practical Assignment - Team 13")

        #afficher le humanUserLogo
        self.humanUserLogo = tk.PhotoImage(file="humanUserLogo.png")
        self.humanUserLogo = self.humanUserLogo.subsample(10, 10)
        self.humanUserLabel = tk.Label(master, image=self.humanUserLogo)
        self.humanUserLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.human_player_label = tk.Label(master, text="Human Player\nScore: 0")
        self.human_player_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        # afficher le computerPlayerLogo
        self.computerPlayerLogo = tk.PhotoImage(file="computerPlayerLogo.png")
        self.computerPlayerLogo = self.computerPlayerLogo.subsample(10, 10)
        self.computerPlayerLabel = tk.Label(master, image=self.computerPlayerLogo)
        self.computerPlayerLabel.grid(row=0, column=6, sticky="w", padx=10, pady=10)

        self.computer_player_label = tk.Label(master, text="Computer Player\nScore: 0")
        self.computer_player_label.grid(row=0, column=5, sticky="e", padx=10, pady=10)

        #afficher le vsLogo
        self.vsLogo = tk.PhotoImage(file="vsLogo.png")
        self.vsLogo = self.vsLogo.subsample(10, 10)
        self.vsLabel = tk.Label(master, image=self.vsLogo)
        self.vsLabel.grid(row=0, column=3, padx=10, pady=10)



    def update_scores(self, human_score, computer_score):
        self.human_player_label.config(text=f"Human Player\nScore: {human_score}")
        self.computer_player_label.config(text=f"Computer Player\nScore: {computer_score}")

    def afficherListe(self, liste):
        #afficher chaque élément de la liste un par un avec 3 espaces entre chaque élément
        self.liste_label = tk.Label(self.master, text="       ".join(str(i) for i in liste))
        self.liste_label.grid(row=1, column=0, columnspan=7, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)

    # Exemple de mise à jour des scores
    game_gui.update_scores(5, 10)
    game_gui.afficherListe(liste)

    root.mainloop()

