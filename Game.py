class Game:
    def __init__(self):
        pass

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

        playmode= input("how many humans will be playing")
        if playmode== 1:
            print("singleplayer")
            
        elif playmode== 2:
            print("multiplayer")
            
        else:
            print ("thats not an option. Try again.")

