from Player import Player
from Game import Game
class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        print(self.gestures)
        player_gesture = input("Pick your gesture")
        for gesture in self.gestures:
            if player_gesture == gesture:
                self.chosen_gesture = player_gesture
                return self.chosen_gesture

        else:
            print("Not a valid gesture.. try again")
            self.choose_gesture()