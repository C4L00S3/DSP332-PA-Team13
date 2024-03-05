import tkinter as tk
import random

liste = [random.randint(1, 9) for i in range(random.randint(15, 25))]
print(len(liste))
class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DSP332 - Practical Assignment - Team 13")

        # Canvas pour les éléments en haut
        self.top_canvas = tk.Canvas(master)
        self.top_canvas.pack(side="top")

        # Afficher le humanUserLogo
        self.humanUserLogo = tk.PhotoImage(file="humanUserLogo.png")
        self.humanUserLogo = self.humanUserLogo.subsample(10, 10)
        self.humanUserLabel = tk.Label(self.top_canvas, image=self.humanUserLogo)
        self.humanUserLabel.pack(side="left", padx=10, pady=10)

        self.human_player_label = tk.Label(self.top_canvas, text="Human Player\nScore: 0", font=("verdana", 12), fg="black")
        self.human_player_label.pack(side="left", padx=10, pady=10)

        # Afficher le vsLogo
        self.vsLogo = tk.PhotoImage(file="vsLogo.png")
        self.vsLogo = self.vsLogo.subsample(8, 8)
        self.vsLabel = tk.Label(self.top_canvas, image=self.vsLogo)
        self.vsLabel.pack(side="left", padx=10, pady=10)

        # Afficher le computerPlayerLogo
        self.computer_player_label = tk.Label(self.top_canvas, text="Computer Player\nScore: 0", font=("verdana", 12), fg="black")
        self.computer_player_label.pack(side="left", padx=10, pady=10)

        self.computerPlayerLogo = tk.PhotoImage(file="computerPlayerLogo.png")
        self.computerPlayerLogo = self.computerPlayerLogo.subsample(10, 10)
        self.computerPlayerLabel = tk.Label(self.top_canvas, image=self.computerPlayerLogo)
        self.computerPlayerLabel.pack(side="left", padx=10, pady=10)
        #Canva pour écrire au dessus de la liste
        self.middle_canvas = tk.Canvas(master)
        self.middle_canvas.pack(side="top", fill="both", expand=True)
        #écrire un texte
        self.texte = tk.Label(self.middle_canvas, text="Actual List of the Numbers", font=("verdana", 18, "bold"), fg="black")
        self.texte.pack(side="left", padx=10, pady=10)
        # Canvas pour la liste au milieu
        self.liste_canvas = tk.Canvas(self.master)
        self.liste_canvas.pack(expand=False, fill="both")
        # Canvas pour les indices des éléments
        self.index_canvas = tk.Canvas(self.master)
        self.index_canvas.pack(expand=True, fill="both")
        #Canvas pour les index
        self.bottom_canvas = tk.Canvas(master)
        self.bottom_canvas.pack(expand=True, fill="both")
        self.texte2 = tk.Label(self.bottom_canvas, text="Index for the actual List", font=("verdana", 18, "bold"),fg="black")
        self.texte2.pack(side="left", padx=10, pady=0)
        #Canvas pour afficher le nom du jouer qui joue
        self.actualPlayer_canvas = tk.Canvas(master)
        self.actualPlayer_canvas.pack()
        self.actualPlayer = tk.Label(self.actualPlayer_canvas, text="Actual Player", font=("verdana", 15), fg="black")
        self.actualPlayer.pack(anchor="center", pady=15)
        #Canvas to display the rules
        self.rules_canvas = tk.Canvas(master)
        self.rules_canvas.pack()
        self.rules = tk.Label(self.rules_canvas, text="Enter the index of the first of the two boxes you wish to merge : ", font=("verdana", 15), fg="black")
        self.rules.pack(anchor="center", pady=0)
        #canva with a spinbox
        self.spin_canvas = tk.Canvas(master)
        self.spin_canvas.pack()
        self.spin = tk.Spinbox(self.spin_canvas, from_=1, to=len(liste)-1, font=("verdana", 15), fg="black")
        self.spin.pack(anchor="center", pady=0)
        #canva with a button
        self.button_canvas = tk.Canvas(master)
        self.button_canvas.pack()
        self.button = tk.Button(self.button_canvas, text="Play !", font=("Verdana", 15), fg="black")
        self.button.pack(anchor="center", pady=10)





    def update_scores(self, human_score, computer_score):
        self.human_player_label.config(text=f"Human Player\nScore: {human_score}")
        self.computer_player_label.config(text=f"Computer Player\nScore: {computer_score}")

    def displayList(self, liste):
        #delete the old elements from the canvas
        self.liste_canvas.delete("all")
        self.index_canvas.delete("all")

        for i, num in enumerate(liste):
            label_num = tk.Label(self.liste_canvas, text=num, font=("Arial", 16, "bold"), fg="black", relief="solid", width=2, height=1)
            label_num.pack(side="left", padx=10, pady=10)

            label_index = tk.Label(self.index_canvas, text=i+1, font=("Arial", 16, "bold"), fg="grey", relief="flat", width=2, height=1)
            label_index.pack(side="left", padx=10, pady=10)

    def displayActualPlayer(self, indexActualPlayer):
        if (indexActualPlayer == 0):
            self.actualPlayer_canvas.delete("all")
            self.actualPlayer = tk.Label(self.actualPlayer_canvas, text="Human Player, it's your turn !", font=("verdana", 18, "bold"), fg="black")
            self.actualPlayer.pack()
        elif (indexActualPlayer == 1):
            self.actualPlayer_canvas.delete("all")
            self.actualPlayer = tk.Label(self.actualPlayer_canvas, text="Computer Player, it's your Turn", font=("verdana", 18, "bold"), fg="black")
            self.actualPlayer.pack()


if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)

    # Exemple de mise à jour des scores
    game_gui.update_scores(5, 10)
    game_gui.displayList(liste)

    root.mainloop()
