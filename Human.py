from Player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = input("Pick a gesture: rock, paper, scissors, lizard, spock")
        if (self.chosen_gesture == " rock" or self.chosen_gesture == " paper" or self.chosen_gesture == " scissors" or self.chosen_gesture == " lizard" or self.chosen_gesture == " spock"):
            pass
        else:
            print("Not a valid gesture.. try again")
            self.choose_gesture()