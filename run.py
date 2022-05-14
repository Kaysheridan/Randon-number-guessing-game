import random  # imports random module which is built-in
import os


def game_instructions():
    """
    First the the player will see which explains how to play the
    game and give the player the option to begin the game
    """
    print("🆁 🅰 🅽 🅳 🅾 🅼   🅽 🆄 🅼 🅱 🅴 🆁 🆂\n")
    print('WELCOME TO RANDOM NUMBERS!\n')
    print('This is a guessing game! There is no guess limit.. The aim of the',
          'game is to guess the number correctly in the least amount of',
          'tries as you can.\n')
    print('The number you are looking for is somewhere between 1 and 1000\n')
    input("ᴘʀᴇss ᴀɴʏ ᴋᴇʏ ᴛᴏ ʙᴇɢɪɴ...")


def game_loop():
    """
    For loop which handles the value errors and logic of the game
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
            txt = "YOU GOT IT! Guesses to beat {} \n"
            print(txt.format(guess_amount))
            break


def play_again():
    """
    Function to give the player an option to play again or quit
    """
    while True:
        print('Think you can do better?...\n')
        input('Press any key to continue\n')
        clear_terminal()
        print('Play again? (A) \n')
        print('Quit (Q) \n')
        choose = input('Make your choice...').lower()
        if choose == 'a':
            clear_terminal()
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
    game_instructions()
    clear_terminal()
    game_loop()
    play_again()


main()
