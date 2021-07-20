from player import Player

class AI(Player):
    def __init__(self):
        self.name = ("CPU")
        self.score = 0

    def increment_score(self):
        return super().increment_score()
