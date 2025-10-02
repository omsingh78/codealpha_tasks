import random

words = ["python", "programming", "hangman", "computer", "keyboard"]


word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6  
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
        
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"Wrong! '{guess}' is not in the word. Attempts left: {attempts}")

    print("Word:", " ".join(guessed_word))

if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)