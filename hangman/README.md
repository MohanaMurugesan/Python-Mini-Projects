# Hangman Game

## Description
A simple Python-based **Hangman game**.  
The game selects a random word, and you try to guess it letter by letter.  
The hangman is drawn step by step with every wrong guess.

## Features
- Random word selection using the `random-word` library.
- **ASCII art** hangman drawing for wrong guesses.
- Tracks guessed letters.
- Shows masked word with underscores.
- Terminal-friendly, optionally centered output.

## How to Play
1. Run `app.py` in a Python environment.
2. Guess letters one at a time.
3. Each wrong guess adds a part to the hangman.
4. Win if you guess all letters before the hangman is complete.

## Requirements
- Python 3.x
- `random-word` library (`pip install random-word`)