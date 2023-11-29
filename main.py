# Import modules to use
from words import palabras
import random
import string

# 1. Welcome
print("Welcome to the game hangman in Python")

# 2. Function to get word
def get_valid_word(palabras):
    word = random.choice(palabras)
    while '-' in word or ' ' in word:
        word = random.choice(palabras)
    return word.upper()

def hangman():
    word = get_valid_word(palabras)
    word_letters = set(word)  # Letras de la palabra
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Lo que el usuario ha adivinado
    lives = 6

    # Bucle principal del juego
    while len(word_letters) > 0 and lives > 0:
        # Letras utilizadas
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        # Mostrar el estado actual de la palabra
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Obtener la entrada del usuario
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # Resta una vida si la letra no está en la palabra
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    # Llega al final del juego
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!!")

# Iniciar el juego
hangman()
