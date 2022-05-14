# Random Numbers
Is a game where the player must guess the random number chosen by the computer, the amount of attempts someone has is limitless but the aim of the game is to guess in the least amount of tries as possible. The number range for the game is between 1 and 1000. 

## Project Purpose
The Purpose of the game is to provide the user with a simple and interactive game through a command-line application. The game is intended to be simple and entertaining while making the user compete against themselves with the feature to try and beat how many guesses you got the correct number in. 


## User Experience 
### App owner goals 
- An app that is clear and easily navigated.
- Gives the user options to input data. 
- Gives the user feedback after data has been input. 
- Clearly explain the rules and function of the app.
- Give the user multiple options to itput or choose a path throughout the app. 

### App user goals 
- An app that is easy to navigate. 
- An app with a clear purpose and directions of use. 
- An option to input data.
- To be given the amount of guesses I got the correct number in. 
- An app that is entertaining and interactive.

## Functional Scope 
- The below chart shoes the logical flow of the Random Numbers game.
<img width="549" alt="Screenshot 2022-05-14 at 08 27 41" src="https://user-images.githubusercontent.com/95246821/168415731-44d29be6-0808-4429-b775-2c7785852200.png">

## Features 
### Welcome Message
- The user is given a welcome messgae followed by instructions on how to play the game.
- The user is then asked to press any key to continue to the game

### The game 
- The user is then asked to take a guess
- If the user guesses a number that is too high they will get a go lower hint 
- If the user guesses a number that is too low they will get a go higher hint. 
- If the user uses anything but an integer for their guess they are met with an error.
- When the user guesses the correct number they get a 'You got it!' message followed by how many guesses they got it in.
- The amount of guesses they got it in is also the amount of guesses they are promted to beat. 

### Play again
- The user is again to press anykey to continue 
- The choice to play again or quit is then given to the player. 
- Choosing to play again brings the user back to take a guess and quit brings the user back to the welcome message. 

## Future Features
- I would like to add the option for the user to turn off hints if they wish to make the game harder. 
- I would like to make the game multiplayer where two players can choose to play against each other and pick the others persons random number and who ever guesses the correct number first wins. 
- I would like to add a login for player who can see their previous game history. 

## Language Used 
- Python 3.0

## Modules & API's Used
- Random 
Module used in the main loop of the game, used to choose a random number for the player to guess. 

- OS 
Module used to create the clear terminal function. This removes all previous inputs and outputs from the terminal, this helps with the flow of the game. 

## User Testing 
- Testing was carried out after each feature was added to ensure the functionality of the game remained intact when code was added edited or removed. 

- User testing was conducted during the development of this project
- As a user I would expect to know what the game is and how to play. This test passed. 
- As a user I would expect the app to continue when I press any key. This test passed. 
- As a user I would expect to the game to begin when I make a guess. This test passed. 
- As a user I would expect to know when my guess is wrong. This test passed. 
- As a user I would expect to know when my guess is correct. This test passed. 
- As a user I would expect to know how many guesses I made to get the correct number. This test passed. 
- As a user I would expect the options to play again or quit to have different functionalities. This test passed. 

## Pep8 Validator
- <img width="1042" alt="Screenshot 2022-05-14 at 09 48 56" src="https://user-images.githubusercontent.com/95246821/168418524-a94cc1c2-b301-450c-a709-ee5448225c77.png">

## Bugs 
### Bugs that occurred during development that are now fixed. 

-  There was an issue with placing the clear terminal at certain points in game when needed, when placed after the break in the game_loop function it would print the 'You got it message' and then immediately clear before the user would have had a chance to read the messgae. This lead me to adding the 'think you can do better' message and 'press any key to continue' input in the play_again function which allowed me to call the clear terminal function when the player would press a key to continue. 

# Deployment 
- Go to the Heroku site.
- Log in.
- Click the "New" button and click "Creat new app"
- Provide a name for the app in the "App name" field.
- Select your region from the dropdown menu.
- Click "Create App".
- Then proceed to the settings tab.
- Click "config vars".
- Enter a KEY of PORT and it's value of 8000. The click "add".
- Next click "Add buildpack".
- The python buildpack needs to be added first followed by the nodejs buildpack.
- After the buildpacks been added, proceed to the deploy tab.
- In the terminal on git hub type "heroku login -i"
- You will then be prompted to input yout log in credentials in the terminal
- It will advise if the log in is successful. 
- Run 'git push heroku main' after any/all changes have be made. 
- Click 'open app' on the Heroku website. 








