import random
import time

def welcome_message():
    print("""
🎉 Welcome to the Number Guessing Game! 🎉
Try to guess the number I'm thinking of between 1 and 100.
You can choose your difficulty level.
""")

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (15 attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard (5 attempts)")
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return 15
        elif choice == "2":
            return 10
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Try again.")

def number_guessing_game():
    welcome_message()
    max_attempts = choose_difficulty()
    secret_number = random.randint(1, 100)
    attempts = 0
    previous_diff = None

    print(f"\nI'm thinking of a number between 1 and 100. You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"\n🎊 Congratulations! You guessed the number {secret_number} in {attempts} attempts! 🎊")
                print("""
                 .-=========-.
                 \'-=======-'/
                 _|   .=.   |_
                ((|  {{1}}  |))
                 \|   /|\   |/
                  \__ '`' __/
                    _`) (`_
                  _/_______\_
                 /___________\\
                """)
                break
            else:
                diff = abs(secret_number - guess)
                if previous_diff is not None:
                    if diff < previous_diff:
                        print("🔥 Warmer! You're getting closer.")
                    elif diff > previous_diff:
                        print("❄️ Colder! You're moving away.")
                    else:
                        print("😐 Same distance as last guess.")
                else:
                    if guess < secret_number:
                        print("⬆️ Too low! Try a higher number.")
                    else:
                        print("⬇️ Too high! Try a lower number.")

                previous_diff = diff
                print(f"Attempts remaining: {max_attempts - attempts}\n")

        except ValueError:
            print("Please enter a valid number!")

    else:
        print(f"\n💀 Game Over! The number was {secret_number}")

def main():
    while True:
        number_guessing_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye 👋")
            break
        print("\n" + "-"*50 + "\n")
        time.sleep(1)

if __name__ == "__main__":
    main()
