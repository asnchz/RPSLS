from AI import Ai
from Human import Human


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        # intro
        self.game_intro()
        self.player_mode()
        # game rounds
        while self.player_one.score < 3 and self.player_two.score <3:
            self.play()
        #end game
        self.display_winner


    def game_intro(self):
        print("Welcome to RPSLS!")
        print("The rules are as follows: each player will pick one of gestures.")
        print("Gesture options are: Rock, Paper, Scissors, Lizard, or spock.")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        

        
    def player_mode(self):
        print("How many humans will be playing?")
        playmode = int(input())
        if playmode== 1:
            self.player_one.name = input("Player 1, enter your name")
            self.player_two = Ai()
        elif playmode== 2:
            self.player_two = Human()
            self.player_two.name = input("Player 2, enter your name")
        else:
            print ("thats not an option. Try again.")

    def player_pick(self):
        print(f"{self.player_one.name} picked {self.player_one.chosen_gesture}")
        print(f"{self.player_two.name} picked {self.player_two.chosen_gesture}")


    def play(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        self.player_pick()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Its a tie")

        elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "scissors":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "scissors" and self.player_two.chosen_gesture =="rock":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture =="paper":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture =="rock":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture =="lizard":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture =="rock":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture =="spock":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture =="rock":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture =="scissors":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        elif self.player_one.chosen_gesture == "scissors" and self.player_two.chosen_gesture=="paper":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture =="lizard":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture =="paper":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture =="spock":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture =="paper":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        elif self.player_one.chosen_gesture == "scissors" and self.player_two.chosen_gesture =="lizard":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture =="scissors":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        elif self.player_one.chosen_gesture == "scissors" and self.player_two.chosen_gesture =="spock":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")
    
        elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture =="scissors":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture =="spock":
            self.player_one.score += 1
            print(self.player_one.name + " wins this round!")

        elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture =="lizard":
            self.player_two.score += 1
            print(self.player_two.name + " wins this round!")

        else:
            print ("thats not an option. Try again.")

    def display_winner(self):
        if self.player_one.score == 2:
            print(self.player_one.name + " wins the game.")
        elif self.player_two.score == 2:
            print(self.player_two.name + " wins the game.")
    

#     player_gesture= input("which gesture do you choose?")


