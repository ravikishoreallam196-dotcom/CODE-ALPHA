import random

# 5 predefined words
words = ["python", "laptop", "college", "india", "keyboard"]

word = random.choice(words)
guessed = []          # correct letters
wrong = 0
max_wrong = 6

print("=== HANGMAN GAME ===")

while wrong < max_wrong:
    # show word with blanks
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)

    # check win
    if "_" not in display:
        print("You won! The word is:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter.")
        continue

    if guess in guessed:
        print("Already guessed that letter.")
        continue

    if guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        wrong += 1
        guessed.append(guess)
        print("Wrong! Remaining chances:", max_wrong - wrong)

else:
    print("\nGame over! The word was:", word)