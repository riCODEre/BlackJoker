# BlackJoker

A blackjack game desktop app where you can compete with a bot. The game features RNG (Random Number Generation) for cards dealt to both the player and the bot. This app is built with Python and the Tkinter GUI framework.

## Features

- Player vs Bot gameplay
- Random card generation
- Virtual betting system
- Simple and intuitive GUI interface
- Score tracking
- Standard blackjack rules
- Card visualization with proper card images

## Screenshots

The game features a red-themed interface with playing cards and game status indicators:
- Player's cards are displayed face up
- Bot's cards are initially hidden (displayed as Yu-Gi-Oh card backs)
- Win/Lose/Tie status is shown with appropriate images

## Requirements

- Python 3.x
- Tkinter module (included with most Python installations)
- Pillow library (for image processing)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ericdreyes/BlackJoker.git
   ```
2. Make sure you have Python installed
3. Navigate to the project directory:
   ```
   cd BlackJoker
   ```
4. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the game using:
   ```
   python newfile.py
   ```

## Usage

1. Launch the game using the installation instructions above
2. Enter a bet amount in the input field
3. Click "Play" to start a new round
4. Click "Hit" to draw another card
5. Click "Stay" to keep your current hand
6. The dealer (bot) will play their turn automatically
7. The winner will be determined based on standard blackjack rules
8. Your money balance will be updated based on the outcome

## Game Rules

- The goal is to get a hand value as close to 21 as possible without going over
- Number cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10 points
- Aces are worth 11 points
- If your hand exceeds 21 points, you "bust" and lose the round
- The bot follows a strategy where it will:
  - Always hit if its hand value is 14 or less
  - Sometimes hit if its hand value is between 15 and 18
  - Usually stand if its hand value is higher

## Project Structure

- `newfile.py` - Main game file containing all game logic and GUI
- `playingcards/` - Directory containing all card images (52 standard playing cards)
- `requirements.txt` - List of Python dependencies
- Various image files:
  - `bg_blackjack.jpg` - Background image
  - `jack_icon.ico` - Application icon
  - `joker.png` - Joker card image
  - `win.jpg`, `lose.jpg`, `tie.jpg` - Game outcome images
  - `yugioh.png` - Card back image for the bot's hidden cards

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author

Created by Eric Delos Reyes (Ricodere)
