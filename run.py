import random  # imports random module which is built-in
import os


print("🆁 🅰 🅽 🅳 🅾 🅼   🅽 🆄 🅼 🅱 🅴 🆁 🆂\n")
print('This is a guessing game, guess the number correctly in',
      'the least amount of tries as you can.\n')
input("PRESS ANY KEY TO BEGIN...")


def game_loop():
    """
    For loop which handles the values errors and logic of the game
    """
    guess_amount = 0
    correct_answer = random.randint(1, 100)

    for guesses in range(100):
        print('Take a guess...')
        guess_amount += 1
        while True:
            try:
                player_guess = int(input())
                break
            except ValueError:
                print("Thats not a number, please enter a number")
        if player_guess < 1:
            print("Please enter a number between 1 and 10")
        elif player_guess > 100:
            print("Please enter a number between 1 and 10")
        elif player_guess > correct_answer:
            print("HINT! Go lower...")
        elif player_guess < correct_answer:
            print("HINT! Go higher...")
        else:
            txt = "YOU GOT IT! Guesses to beat {}"
            print(txt.format(guess_amount))
            break  # Correct number guessed
            

def play_again():
    """
    Function to give the player an option to play again or quit
    """
    while True:
        print('Play again? (A) \n')
        print('Quit (Q) \n')
        choose = input('Think you can do better? ').lower()
        if choose == 'a':
            game_loop()
        elif choose == 'q':
            return False
        else:
            print(f'Not a correct choice : {choose}')
            clear_terminal()


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
    play_again()


main()
