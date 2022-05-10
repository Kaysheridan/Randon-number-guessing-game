import random  # imports random module which is built-in
import os

correct_answer = random.randint(1, 10)
GUESS_AMOUNT = 0


print("Welcome to random numbers\n")
print("""
This is a guessing game, guess the number correctly in the
least amount of tries as you can.\n""")
input("PRESS ENTER TO BEGIN...")


def game_loop():
    """
    The First page to appear on the terminal, used to present the player
    with print statements
    """
 #   while True:
 #       player_guess = int(input("Take a guess.."))
 #      guess_amount = +1
 #       if correct_answer != player_guess:
 #           print("Woopsies, try again...")
 #           if correct_answer < player_guess:
 #               txt = "You are getting warmer the right number is between 1 and {}"
 #               print(txt.format(player_guess))
 #           else:
 #               txt_two = "You're getting warmer the right number is between {} and 10"
 #               print(txt_two.format(player_guess))
 #       else:
 #           txt_three = "YOU GOT IT! Guesses to beat {}"
 #           print(txt_three.format(guess_amount))
 #           break
    for guesses in range(10):
        print('Take a guess...')
        while True:
            try:
                player_guess = int(input())
                break
            except ValueError:
                print("Thats not a number, please enter a number")
        if player_guess < 1:
            print("Please enter a number between 1 and 10")
        elif player_guess > 10:
            print("Please enter a number between 1 and 10")
        elif player_guess > correct_answer:
            print("HINT! Go lower...")
        elif player_guess < correct_answer:
            print("HINT! Go higher...")
        else:
            txt = "YOU GOT IT! guesses to beat {}"
            print(txt.format(GUESS_AMOUNT))
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
    clear_terminal()
    game_loop()


main()
