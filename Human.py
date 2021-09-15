from Player import Player
<<<<<<< HEAD

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = input("Pick a gesture: rock, paper, scissors, lizard, spock")
        if (self.chosen_gesture == " rock" or self.chosen_gesture == " paper" or self.chosen_gesture == " scissors" or self.chosen_gesture == " lizard" or self.chosen_gesture == " spock"):
            pass
=======
class Human(Player):
    def __init__(self):
        super().__init__()
        player_gesture = input("Pick your gesture")
        for self.gestures in self.gestures:
            if player_gesture == self.gestures:
                self.chosen_gesture = player_gesture
                return self.chosen_gesture

>>>>>>> 2d95655129cf06bcb542b3e4ce7f7c19ee377852
        else:
            print("Not a valid gesture.. try again")
            self.choose_gesture()