# U.S. States Game

This is a U.S. States guessing game built using Python's `turtle` module. The goal of the game is to guess all 50 U.S. states by entering state names. Each correct guess displays the state name on a U.S. map.

## Project Structure

- **usstategame.py**: Contains the `USStateGame` class, which handles the game logic, including input handling, checking correct answers, and displaying the guessed states on the map.
- **main.py**: The main file to start the game. It initializes the screen, loads the U.S. map, and starts the game.
- **50_states.csv**: A CSV file containing the names and coordinates of all 50 U.S. states for plotting on the map.
- **blank_states_img.gif**: A U.S. map image used as the background for the game.

## How It Works

1. The game displays a blank U.S. map.
2. Users are prompted to enter the name of a U.S. state.
3. If the guess is correct, the state's name is displayed on the map at its correct location.
4. The game continues until all 50 states are guessed correctly.
