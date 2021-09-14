from Player import Player
from Game import Game

class Round:
    def __init__(self):
        self.round_min= 3
        
    def all_round_winner(self):
        if self.player_one== 3:
            print ("you are the winner!")
        elif self.player_one== 2:
            print ("you are the winner!")
        elif self.player_two== 3:
            print ("you are the winner!")
        elif self.player_two== 2:
            print ("you are the winner!")

