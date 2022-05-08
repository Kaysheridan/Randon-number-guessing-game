import random  # imports random module which is built-in
import os


def game_description():
    """
    The First page to appear on the terminal, used to present the player
    with print statements
    """
    print("Welcome to random numbers\n")
    print(""" This is a guessing game, guess the number correctly in the
    least amount of tries as you can.""")
    input("press enter to begin")
    clear_terminal()


def game_loop():
    """
    While loop that controls the loop and hints of the game 
    """
    correct_answer = random.randint(1, 10)
    guesses = 0
    while True:
        player_guess = int(input("Take a guess.."))
        guesses = +1
        if correct_answer != player_guess:
            print("Woopsies, try again...")
            if correct_answer < player_guess:
                txt = "You are getting warmer the right number is between 1 and {}"
                print(txt.format(player_guess))
            else:
                txt_two = "You're getting warmer the right number is between {} and 10"
                print(txt_two.format(player_guess))
        else:
            txt_three = "YOU GOT IT! Guesses to beat {}"
            print(txt_three.format(guesses))
            break


def validate_guess():
    """
    Function to give error message if anything bar a number is attempted as a
    guess and also to make sure the attempted guess is within 0-100
    """


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
    clear_terminal()
    game_description()
    game_loop()
    validate_guess()


main()
