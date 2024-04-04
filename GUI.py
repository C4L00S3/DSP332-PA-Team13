import tkinter as tk
import random
class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("DSP332 - Practical Assignment - Team 13")
        self.startPlayer = 0
        self.chooseAlgorithm = 0
        self.gameInfo = []
        self.hasChosen = False
        self.indexToMerge = None
        self.hasPlayed = False
        self.indexActualPlayer = None


    def setHasChosen(self, hasChosen):
        self.hasChosen = hasChosen
    def getHasChosen(self):
        return self.hasChosen
    def setStartPlayer(self, startPlayer):
        self.startPlayer = startPlayer
    def getStartPlayer(self):
        return self.startPlayer
    def setChooseAlgorithm(self, chooseAlgorithm):
        self.chooseAlgorithm = chooseAlgorithm
    def getChooseAlgorithm(self):
        return self.chooseAlgorithm
    def setGameInfo(self, gameInfo):
        self.gameInfo = gameInfo
    def getGameInfo(self):
        return self.gameInfo
    def getIndex(self):
        return self.indexToMerge
    def setIndex(self, indexToMerge):
        self.indexToMerge = indexToMerge
    def getHasPlayed(self):
        return self.hasPlayed
    def setHasPlayed(self, hasPlayed):
        self.hasPlayed = hasPlayed
    def setIndexActualPlayer(self, indexActualPlayer):
        self.indexActualPlayer = indexActualPlayer
    def getIndexActualPlayer(self):
        return self.indexActualPlayer

    def displayStartGameScreen(self):
            for widget in self.master.winfo_children():
                widget.destroy()

            #title canva
            self.title_canvas = tk.Canvas(self.master)
            self.title_canvas.pack()
            self.title = tk.Label(self.title_canvas, text="Welcome to the Game", font=("verdana", 20, "bold"), fg="black")
            self.title.pack(anchor="center", pady=15)
            #canva to ask the size of the list
            self.size_canvas = tk.Canvas(self.master)
            self.size_canvas.pack()
            self.size = tk.Label(self.size_canvas, text="Enter the size of the list (between 15 and 25) : ", font=("verdana", 15), fg="black")
            self.size.pack(anchor="center", pady=0)
            #canva with a spinbox that store the size of the list in the variable listSize
            self.spin_canvas = tk.Canvas(self.master)
            self.spin_canvas.pack()
            self.spin = tk.Spinbox(self.spin_canvas, from_=15, to=25, font=("verdana", 15), fg="black")
            self.spin.pack(anchor="center", pady=0)
            #canva to choose who start the game (user or computer)
            self.who_start_canvas = tk.Canvas(self.master)
            self.who_start_canvas.pack()
            self.who_start = tk.Label(self.who_start_canvas, text="Who start the game ? ", font=("verdana", 15), fg="black")
            self.who_start.pack(anchor="center", pady=0)
            #selection of the player who start the game
            self.who_start_button_canvas = tk.Canvas(self.master)
            self.who_start_button_canvas.pack()
            #button to choose the user, startPlayer = 0 if the user start the game, 1 if the computer start the game
            self.user_button = tk.Button(self.who_start_button_canvas, text="User", font=("Verdana", 15), fg="black", command=lambda: self.setStartPlayer(0))
            self.user_button.pack(side="left", padx=10, pady=10)
            self.computer_button = tk.Button(self.who_start_button_canvas, text="Computer", font=("Verdana", 15), fg="black", command=lambda: self.setStartPlayer(1))
            self.computer_button.pack(side="left", padx=10, pady=10)
            #canva to choose between the Minimax and Alpha-Beta algorithm
            self.algorithm_canvas = tk.Canvas(self.master)
            self.algorithm_canvas.pack()
            self.algorithm = tk.Label(self.algorithm_canvas, text="Choose the algorithm : ", font=("verdana", 15), fg="black")
            self.algorithm.pack(anchor="center", pady=0)
            #selection of the algorithm
            self.algorithm_button_canvas = tk.Canvas(self.master)
            self.algorithm_button_canvas.pack()
            #button to choose the Minimax algorithm, algorithm = 0 if the Minimax algorithm is chosen, 1 if the Alpha-Beta algorithm is chosen
            self.minimax_button = tk.Button(self.algorithm_button_canvas, text="Minimax", font=("Verdana", 15), fg="black", command=lambda: self.setChooseAlgorithm(0))
            self.minimax_button.pack(side="left", padx=10, pady=10)
            self.alpha_beta_button = tk.Button(self.algorithm_button_canvas, text="Alpha-Beta", font=("Verdana", 15), fg="black", command=lambda: self.setChooseAlgorithm(1))
            self.alpha_beta_button.pack(side="left", padx=10, pady=10)
            #button to start the game
            self.start_button_canvas = tk.Canvas(self.master)
            self.start_button_canvas.pack()

            # Bouton pour démarrer la partie
            self.start_button = tk.Button(self.start_button_canvas, text="Start Game", font=("Verdana", 15), fg="black",
                                          command=self.startGame)
            self.start_button.pack()
    def startGame(self):
        size_of_list = int(self.spin.get())
        start_player = self.getStartPlayer()
        chosen_algorithm = self.getChooseAlgorithm()

        game_info = [size_of_list, start_player, chosen_algorithm]
        self.setGameInfo(game_info)
        self.setHasChosen(True)
        print("GAME INFO : ", self.getGameInfo())

    def displayGameScreen(self, master, game, indexActualPlayer, playerList):
        for widget in self.master.winfo_children():
            widget.destroy()
        # Canvas pour les éléments en haut
        self.top_canvas = tk.Canvas(master)
        self.top_canvas.pack(side="top")

        # Afficher le humanUserLogo
        self.humanUserLogo = tk.PhotoImage(file="humanUserLogo.png")
        self.humanUserLogo = self.humanUserLogo.subsample(10, 10)
        self.humanUserLabel = tk.Label(self.top_canvas, image=self.humanUserLogo)
        self.humanUserLabel.pack(side="left", padx=10, pady=10)

        self.human_player_label = tk.Label(self.top_canvas, text="Human Player\nScore: 0", font=("verdana", 12),
                                           fg="black")
        self.human_player_label.pack(side="left", padx=10, pady=10)

        # Afficher le vsLogo
        self.vsLogo = tk.PhotoImage(file="vsLogo.png")
        self.vsLogo = self.vsLogo.subsample(8, 8)
        self.vsLabel = tk.Label(self.top_canvas, image=self.vsLogo)
        self.vsLabel.pack(side="left", padx=10, pady=10)

        # Afficher le computerPlayerLogo
        self.computer_player_label = tk.Label(self.top_canvas, text="Computer Player\nScore: 0", font=("verdana", 12),
                                              fg="black")
        self.computer_player_label.pack(side="left", padx=10, pady=10)

        self.computerPlayerLogo = tk.PhotoImage(file="computerPlayerLogo.png")
        self.computerPlayerLogo = self.computerPlayerLogo.subsample(10, 10)
        self.computerPlayerLabel = tk.Label(self.top_canvas, image=self.computerPlayerLogo)
        self.computerPlayerLabel.pack(side="left", padx=10, pady=10)
        self.update_scores(playerList[0].getScore(), playerList[1].getScore())
        # Canva pour écrire au dessus de la liste
        self.middle_canvas = tk.Canvas(master)
        self.middle_canvas.pack(side="top", fill="both", expand=True)
        # écrire un texte
        self.texte = tk.Label(self.middle_canvas, text="Actual List of the Numbers", font=("verdana", 18, "bold"),
                              fg="black")
        self.texte.pack(side="left", padx=10, pady=10)
        # Canvas pour la liste au milieu
        self.liste_canvas = tk.Canvas(self.master)
        self.liste_canvas.pack(expand=False, fill="both")
        #afficher la liste
        # Canvas pour les indices des éléments
        self.index_canvas = tk.Canvas(self.master)
        self.index_canvas.pack(expand=True, fill="both")
        # parcourir les anciens éléments du canva et les supprimer
        liste = game.getRandomNumberList()
        self.liste_canvas.delete("all")
        self.index_canvas.delete("all")
        print("LISTE : ", liste)
        for i, num in enumerate(liste):
            label_num = tk.Label(self.liste_canvas, text=num, font=("Arial", 16, "bold"), fg="black", relief="solid",
                                 width=2, height=1)
            label_num.pack(side="left", padx=10, pady=10)

            label_index = tk.Label(self.index_canvas, text=i + 1, font=("Arial", 16, "bold"), fg="grey", relief="flat",
                                   width=2, height=1)
            label_index.pack(side="left", padx=10, pady=10)
            self.master.update()
        # Canvas pour les index
        self.bottom_canvas = tk.Canvas(master)
        self.bottom_canvas.pack(expand=True, fill="both")
        self.texte2 = tk.Label(self.bottom_canvas, text="Index for the actual List", font=("verdana", 18, "bold"),
                               fg="black")
        self.texte2.pack(side="left", padx=10, pady=0)
        # Canvas to display the actual player
        self.actualPlayer_canvas = tk.Canvas(master)
        self.actualPlayer_canvas.pack()
        self.actualPlayer = tk.Label(self.actualPlayer_canvas, text="Actual Player", font=("verdana", 15), fg="black")
        self.actualPlayer.pack(anchor="center", pady=15)
        self.actualPlayer_canvas.delete("all")

        if self.getIndexActualPlayer() == 0:
            self.actualPlayer_canvas.delete("all")
            self.actualPlayer = tk.Label(self.actualPlayer_canvas, text="Human Player, it's your turn !",
                                         font=("verdana", 16, "bold"), fg="black")
            self.actualPlayer.pack()
            self.rules_canvas = tk.Canvas(master)
            self.rules_canvas.pack()
            self.rules = tk.Label(self.rules_canvas,
                                  text="\nEnter the index of the first of the two boxes you wish to merge : ",
                                  font=("verdana", 15), fg="black")
            self.rules.pack(anchor="center", pady=0)

            self.spin_canvas = tk.Canvas(master)
            self.spin_canvas.pack()
            self.spin = tk.Spinbox(self.spin_canvas, from_=1, to=len(game.getRandomNumberList()) - 1,
                                   font=("verdana", 15), fg="black")
            self.spin.pack(anchor="center", pady=0)
        elif self.getIndexActualPlayer() == 1:
            self.actualPlayer_canvas.delete("all")
            self.actualPlayer = tk.Label(self.actualPlayer_canvas, text="Computer Player, it's your turn !\n",
                                         font=("verdana", 16, "bold"), fg="black")
            self.actualPlayer.pack()
            #canva to display the rules
            self.rules_canvas = tk.Canvas(master)
            self.rules_canvas.pack()
            self.rules = tk.Label(self.rules_canvas,text="When it's Computer's turn, press play to let the AI play.\n",font=("verdana", 13), fg="black")
            self.rules.pack(anchor="center", pady=0)

        self.button_canvas = tk.Canvas(master)
        self.button_canvas.pack()
        self.button = tk.Button(self.button_canvas, text="Play !", font=("Verdana", 15), fg="black", command=lambda: self.playYourTurn())
        self.button.pack(anchor="center", pady=10)
        self.master.update()

    def playYourTurn(self):
        print("ENTREE DANS LA FONCTION PLAY YOUR TURN")
        indexActualPlayer = self.getIndexActualPlayer()
        print("Actual Player : ", indexActualPlayer)
        if indexActualPlayer == 0:
            self.setHasPlayed(True)
            print("ENTREE DANS LA FONCTION PLAY YOUR TURN")
            indexToMerge = int(self.spin.get())
            self.setIndex(indexToMerge)
            print("INDEX TO MERGE : ", self.indexToMerge)
            print("FIN DE LA FONCTION PLAY YOUR TURN")
        elif indexActualPlayer == 1:
            self.setHasPlayed(True)
            print("AI PLAY HIS TURN")

    def endGameScreen(self):
        pass

    def update_scores(self, human_score, computer_score):
        self.human_player_label.config(text=f"Human Player\nScore: {human_score}")
        self.computer_player_label.config(text=f"Computer Player\nScore: {computer_score}")

    """def updateList(self, liste):
        #parcourir les anciens éléments du canva et les supprimer
        self.liste_canvas.delete("all")
        self.index_canvas.delete("all")
        print("LISTE : ", liste)
        for i, num in enumerate(liste):
            label_num = tk.Label(self.liste_canvas, text=num, font=("Arial", 16, "bold"), fg="black", relief="solid", width=2, height=1)
            label_num.pack(side="left", padx=10, pady=10)

            label_index = tk.Label(self.index_canvas, text=i+1, font=("Arial", 16, "bold"), fg="grey", relief="flat", width=2, height=1)
            label_index.pack(side="left", padx=10, pady=10)
            self.master.update()


    def displayActualPlayer(self, indexActualPlayer):
        self.actualPlayer_canvas.delete("all")
        self.master.update()
        if (indexActualPlayer == 0):
            self.actualPlayer_canvas.delete("all")
            self.actualPlayer = tk.Label(self.actualPlayer_canvas, text="Human Player, it's your turn !", font=("verdana", 16, "bold"), fg="black")
            self.actualPlayer.pack()
        elif (indexActualPlayer == 1):
            self.actualPlayer_canvas.delete("all")
            self.actualPlayer = tk.Label(self.actualPlayer_canvas, text="Computer Player, it's your Turn", font=("verdana", 16, "bold"), fg="black")
            self.actualPlayer.pack()

    def updateGUI(self, randomNumberList, indexActualPlayer, playerList):
        self.updateList(randomNumberList)
        self.master.update()
        self.displayActualPlayer(indexActualPlayer)
        self.master.update()
        self.update_scores(playerList[0].getScore(), playerList[1].getScore())
        self.master.update()"""




"""if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GUI(root)

    # Exemple de mise à jour des scores
    game_gui.update_scores(5, 10)
    game_gui.displayList(liste)

    root.mainloop()"""
