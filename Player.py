class Player:
    def __init__(self):
        self.score = 0

    def getScore(self):
        return self.score

    def setScore(self, points):
        self.score += points
