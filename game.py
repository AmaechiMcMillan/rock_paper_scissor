from player import Player 


class Game:
    def __init__(self):
        self.player1 = "Jimbo"
        self.player2 = "Henry"

    def display_welcome(self):
        print(f"Welcome to RPSLS!!!")

    def start_game(self):
        self.player1.increment_score()
        self.player2.increment_score() 

    def run_game(self):
        self.display_welcome() 
        self.single_player()
        self.multiplayer()
