from Player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
    
    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        
=======
        rand_gest= random.choice(self.gestures)
        print(rand_gest)
>>>>>>> 2d95655129cf06bcb542b3e4ce7f7c19ee377852
