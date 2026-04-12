import random

# Predefined word list
words = ["python", "random", "string", "loops", "guess"]

# Randomly select a word
word = random.choice(words)

# Game state
guessed_letters = []
wrong_guesses = []
max_wrong = 6

print("=" * 40)
print("       WELCOME TO HANGMAN!")
print("=" * 40)
print(f"The word has {len(word)} letters.")
print(f"You have {max_wrong} incorrect guesses allowed.\n")

# Main game loop
while len(wrong_guesses) < max_wrong:
    # Build and display the current word state
    display = ""
    all_guessed = True
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
            all_guessed = False

    print("Word: " + display.strip())

    # Check win condition
    if all_guessed:
        print("\nYou won!")
        break

    # Show wrong guesses and remaining attempts
    if wrong_guesses:
        print("Wrong letters: " + ", ".join(wrong_guesses))
    print(f"Incorrect guesses remaining: {max_wrong - len(wrong_guesses)}")

    # Get player input
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    # Check for duplicate guess
    if guess in guessed_letters or guess in wrong_guesses:
        print("You already guessed that letter. Try again.\n")
        continue

    # Process the guess
    if guess in word:
        guessed_letters.append(guess)
        print(f"Correct! '{guess}' is in the word.\n")
    else:
        wrong_guesses.append(guess)
        print(f"Wrong! '{guess}' is not in the word.\n")

# Check lose condition
if len(wrong_guesses) >= max_wrong:
    print("\nWord: " + " ".join(word))
    print(f"\nYou lost! The word was: {word}")
