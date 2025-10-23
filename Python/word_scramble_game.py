#!/usr/bin/env python3
"""
Word Scramble Game
------------------
A simple word guessing game.
The computer scrambles a word, and you have to guess the original word.
"""

import random
import time

WORDS = [
    "python", "hacker", "developer", "variable", "function", "keyboard",
    "algorithm", "internet", "software", "hardware", "programming",
    "socket", "network", "cybersecurity", "machine", "learning",
    "data", "science", "github", "openai"
]

def scramble_word(word):
    """Shuffle letters in the word"""
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def play_round():
    """Play a single round of the game"""
    word = random.choice(WORDS)
    scrambled = scramble_word(word)
    print(f"\n🔤 Scrambled word: {scrambled}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").strip().lower()
        if guess == word:
            print("✅ Correct! Great job!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Wrong! Try again. Attempts left: {attempts}")
            else:
                print(f"💡 Out of attempts! The correct word was: {word}")
                return False

def main():
    print("=" * 40)
    print("🎮 Welcome to the Word Scramble Game!")
    print("=" * 40)
    print("You’ll get 3 tries to guess the correct word.\n")

    score = 0
    rounds = 0

    while True:
        rounds += 1
        if play_round():
            score += 1
        time.sleep(0.5)

        cont = input("\nDo you want to play again? (y/n): ").strip().lower()
        if cont != 'y':
            break

    print("\n🏁 Game Over!")
    print(f"Rounds played: {rounds}")
    print(f"Your final score: {score}")
    print("Thanks for playing!\n")

if __name__ == "__main__":
    main()
