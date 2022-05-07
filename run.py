import random 
import os


def game_description():
    """
    The First page to appear on the terminal, used to present the player with print 
    statements.
    """
    print("Welcome to random numbers\n")
    print(""" This is a numbers game, guess the number correctly in the
    least amount of tries as you can.""")
    input("press enter to begin")
    clear_terminal()

        
def number_generator():
    """
    Function to generate the random number the player must guess correctly
    """
    correct_answer = random.randint(1,100)
    player_guess = int(input("Take a guess.."))


game_description()
number_generator()


def clear_terminal():
    """
    Fuction that is called each time we need to clear the terminal throughout 
    the application when necessary.
    """
    os.system("clear")
