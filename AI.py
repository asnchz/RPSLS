from Player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        rand_gest= random.choice(self.gestures)
        print(rand_gest)