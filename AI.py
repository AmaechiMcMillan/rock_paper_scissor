from player import Player

class AI(Player):
    def __init__(self):
        self.name = ("CPU")
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = ""
        self.choose_gesture = ()
        self.score = 0

    def choose_gesture(self):
        gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = map(
            gestures, ("rock", "paper", "scissors", "lizard", "spock"))
        return len(self.gestures)
        
    def increment_score(self):
        return super().increment_score()
