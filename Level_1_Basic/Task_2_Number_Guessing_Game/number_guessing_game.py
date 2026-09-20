import random


def number_guessing_game():
    print("=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)

    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low!")

            elif guess > secret_number:
                print("Too high!")

            else:
                print(f"\nCongratulations! You guessed the number!")
                print(f"The number was {secret_number}.")
                print(f"You used {attempts} attempt(s).")
                return

            remaining = max_attempts - attempts

            if remaining > 0:
                print(f"Attempts remaining: {remaining}")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\nGame over!")
    print(f"The correct number was {secret_number}.")


if __name__ == "__main__":
    number_guessing_game()