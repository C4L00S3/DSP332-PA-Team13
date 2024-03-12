class Player:
 # Constructor to initialize a player object with the given
    def __init__(self, name):
        self.name = name
        self.score = 0
        
# Create two players - p1 and p2
    def get_score(self):
        return self.score
    
# Method to increase score by 5 for the player
    def add_score(self, points):
        self.score += points
        
# Class methods
    def move(self, input_index):
        # Your logic for player move goes here
        pass  # Placeholder for the move logic
