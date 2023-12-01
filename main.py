import random
from flask import Flask, render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta básica
@app.route('/')
def hangman():
    return render_template('index.html')

# Punto de entrada para la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)

import string

from resources import palabras
from resources import hangmanASCI

def welcome():
    print("Welcome to the hangman game in Python")

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Convertir la palabra a mayúsculas

def display_word(word, guessed_letters):
    display = 'Word to guess: '
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def display_incorrect_guesses(incorrect_guesses):
    return 'Letras incorrectas: ' + ' '.join(incorrect_guesses)


def hangman():
    welcome()

    word_to_guess = get_valid_word(palabras)
    word_letters = set(word_to_guess)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    incorrect_guesses = set()
    lives = 6

    while lives > 0:
        # Monito Hangaman en ASCI
        print(hangmanASCI[lives]);

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)
        print(display_incorrect_guesses(incorrect_guesses))

        guess = input("Guess a letter: ").upper()  # Convertir la letra a mayúsculas

        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess not in word_letters:
                lives -= 1
                incorrect_guesses.add(guess)

            if set(word_letters).issubset(guessed_letters):
                print(hangmanASCI[lives]);
                print("Congratulations! You guessed the word:", word_to_guess)
                break
        elif guess in guessed_letters:
            print("You have already guessed that letter, try again.")
        else: 
            print("Invalid input. Please enter a valid letter.")

        print("Lives left:", lives)

        if lives == 0:
            print(hangmanASCI[lives]);
            print("Sorry, you ran out of lives. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
