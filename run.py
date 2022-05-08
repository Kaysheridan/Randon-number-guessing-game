import random 
import os


def game_description():
    """
    The First page to appear on the terminal, used to present the player with print 
    statements.
    """
    print("Welcome to random numbers\n")
    print(""" This is a guessing game, guess the number correctly in the 
    least amount of tries as you can.""")
    input("press enter to begin")
    

correct_answer = random.randint(0,10)
guesses = 0

while True:
    player_guess = int(input("Take a guess.."))
    guesses = +1

    if correct_answer != player_guess:
        print("Woopsies, try again...")

        if correct_answer < player_guess:
            TXT = "You are getting warmer the right number is between 1 and {}"
            print(TXT.format(player_guess))
        else:
            TXT_TWO = "You're getting warmer the right number is between {} and 10"
            print(TXT_TWO.format(player_guess))
    else:
        TXT_THREE = "YOU GOT IT! Guesses to beat {}"
        print(TXT_THREE.format(player_guess))
        break
    

def clear_terminal():
    """
    Fuction that is called each time we need to clear the terminal throughout 
    the application when necessary.
    """
    os.system("clear")


def main():
    """
    Run all program functions
    """
    game_description()
    clear_terminal()


main()
