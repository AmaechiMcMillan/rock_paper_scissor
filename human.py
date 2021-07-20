from player import Player

class Human(Player):
    def __init__(self):
        self.name = ("Jimbo")
        self.score = 0

    def show_name(self):
        return self.name 
    
    def increment_score(self):
        return super().increment_score()
