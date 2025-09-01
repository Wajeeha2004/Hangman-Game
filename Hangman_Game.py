import random

# Small word list
words = ["apple", "banana", "grape", "mango", "orange"]
word = random.choice(words)

# Game setup
hidden = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in hidden:
    print("\nWord:", " ".join(hidden))
    guess = input("Guess a letter: ")

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

# Result
if "_" not in hidden:
    print("You win! Word was:", word)
else:
    print("You lose! Word was:", word)
