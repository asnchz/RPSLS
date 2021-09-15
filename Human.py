from Player import Player
class Human(Player):
    def __init__(self):
        super().__init__()
        player_gesture = input("Pick your gesture")
        for self.gestures in self.gestures:
            if player_gesture == self.gestures:
                self.chosen_gesture = player_gesture
                return self.chosen_gesture

        else:
            print("Not a valid gesture.. try again")
            self.choose_gesture()