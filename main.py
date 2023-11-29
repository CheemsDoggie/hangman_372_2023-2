import random
import string

from words import palabras

def welcome():
    print("Welcome to the hangman game in Python")

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Convertir la palabra a mayúsculas

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    welcome()

    word_to_guess = get_valid_word(palabras)
    word_letters = set(word_to_guess)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    lives = 6

    print("Word to guess:", display_word(word_to_guess, guessed_letters))

    while lives > 0:
        guess = input("Guess a letter: ").upper()  # Convertir la letra a mayúsculas

        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess not in word_letters:
                lives -= 1

            current_display = display_word(word_to_guess, guessed_letters)
            print(current_display)

            if set(word_letters).issubset(guessed_letters):
                print("Congratulations! You guessed the word:", word_to_guess)
                break
        else:
            print("Invalid input. Please enter a valid letter.")

        print("Lives left:", lives)

        if lives == 0:
            print("Sorry, you ran out of lives. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
