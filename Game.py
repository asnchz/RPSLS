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


        #end game

        

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
            self.player_one.name = input("please enter your name")
            self.player_two = Ai()
            if rand_gesture== "rock" & choose_gesture=="scissors":
            
            elif rand_gesture== "scissors" & choose_gesture=="rock":
            
            elif rand_gesture== "rock" & choose_gesture=="paper":

            elif rand_gesture== "paper" & choose_gesture=="rock":
            
            elif rand_gesture== "rock" & choose_gesture=="lizard":
            
            elif rand_gesture== "lizard" & choose_gesture=="rock":
            
            elif rand_gesture== "rock" & choose_gesture=="spock":
            
            elif rand_gesture== "spock" & choose_gesture=="rock":
            
            elif rand_gesture== "paper" & choose_gesture=="scissors":
            
            elif rand_gesture== "scissors" & choose_gesture=="paper":
            
            elif rand_gesture== "paper" & choose_gesture=="lizard":
            
            elif rand_gesture== "lizard" & choose_gesture=="paper":

            elif rand_gesture== "paper" & choose_gesture=="spock":
            
            elif rand_gesture== "spock" & choose_gesture=="paper":

            elif rand_gesture== "scissors" & choose_gesture=="lizard":
            
            elif rand_gesture== "lizard" & choose_gesture=="scissors":

            elif rand_gesture== "scissors" & choose_gesture=="spock":
            
            elif rand_gesture== "spock" & choose_gesture=="scissors":

            elif rand_gesture== "lizard" & choose_gesture=="spock":

            elif rand_gesture== "spock" & choose_gesture=="lizard":

            elif rand_gesture== "" & choose_gesture=="":

            elif rand_gesture== "" & choose_gesture=="":    

        elif playmode== 2:
            self.player_two = Human()
            user_one_name= input("enter player ones name")
            user_two_name= input("enter player twos name")
        else:
            print ("thats not an option. Try again.")

    

#     player_gesture= input("which gesture do you choose?")


