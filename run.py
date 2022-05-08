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
    

def number_generator():
    """
    Function to generate the random number the player must guess correctly
    """
    

correct_answer = random.randint(1,10)
guesses = 0

while(True):
    player_guess = int(input("Take a guess.."))
    guesses = +1

    if correct_answer != player_guess:
        print("Woopsies, try again...")

        if correct_answer < player_guess:
            print("You are getting warmer the right number is between 0 and {}".format(player_guess))
        else:
            print("You are getting warmer the right number is between 0 and {}".format(player_guess))
    else:
        print("YOU GOT IT! Guesses to beat {}".format(guesses))
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
    number_generator() 
    clear_terminal()


main()
