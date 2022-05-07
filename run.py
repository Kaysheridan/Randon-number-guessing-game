import random 


def game_description():
    """
    The First page to appear on the terminal, welcomes and then explains the game
    to the player. Askes the player to input their name.
    """
    print("Welcome to random numbers\n")
    print(""" This is a numbers game, guess the number correctly in the
    least amount of tries as you can.""")
    input("press enter to begin")


def number_generator():
    """
    Function to generate the random number the player must guess correctly
    """
    correct_answer = random.randint(1,100)
    player_guess = int(input("Take a guess.."))



game_description()
number_generator()


