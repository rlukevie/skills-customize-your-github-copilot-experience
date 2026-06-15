# 📘 Assignment: Games in Python

## 🎯 Objective

In this assignment, you will build a text-based Hangman game in Python. You will practice using variables, loops, conditionals, and string operations to create an interactive game.

## 📝 Tasks

### 🛠️	Build the Core Hangman Loop

#### Description
Create the main game flow where a hidden word is chosen, the player enters guesses, and the game continues until the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of words.
- Ask the player to guess one letter at a time.
- Display the current progress of the word using underscores for unknown letters.


### 🛠️	Handle Game Rules and Results

#### Description
Add game rules for valid guesses, track wrong attempts, and print a final outcome message.

#### Requirements
Completed program should:

- Decrease remaining attempts only when the guessed letter is not in the word.
- Prevent repeated guesses from counting as extra incorrect attempts.
- End with a clear win or lose message and reveal the full word.
