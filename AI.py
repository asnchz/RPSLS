from Player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
    
    def ai_gesture(self):
        rand_gest= random.choice(self.gestures)
        print(rand_gest)