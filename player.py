from AI import AI
from human import Human


class Player:
    def __init__(self):
        self.name = ""
        self.score = 0

    def increment_score(self):
        self.score += 1
