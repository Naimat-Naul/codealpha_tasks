import random

def hangman():
    words = ['python', 'hangman', 'programming', 'developer', 'software', 'inheritance', 'condition', 'internet', 
             'engineer', 'penguin', 'kangaroo', 'parrot', 'castle', 'desert', 'island', 'valley', 'waterfall', 
             'rabbit', 'tiger', 'elephant', 'giraffe', 'monkey', 'garden', 'school', 'bridge', 'market', 'village']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts_left = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(" ".join(guessed_word))
    
    while attempts_left > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            if attempts_left == 1:
                print(f"Wrong guess! '{guess}' is not in the word. Just 1 attempt left.\nPoor man is gonna die because of you!")
            else:
                print(f"Wrong guess! '{guess}' is not in the word. Attempts left: {attempts_left}")
        
        print(" ".join(guessed_word))
    
    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")


hangman()
