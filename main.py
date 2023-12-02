import random
import string
from resources import palabras
from resources import hangmanASCI
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

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
            display += f'{Fore.GREEN}{letter} '  # Letras correctas en verde
        else:
            display += f'{Fore.WHITE}_ '  # Letras no adivinadas en blanco
    return display.strip()

# Función para cargar estadísticas desde un archivo
def load_stats():
    try:
        with open("stats.txt", "r") as file:
            stats = file.readlines()  
            wins, losses = map(int, stats)  
            return wins, losses  
    except FileNotFoundError:  
        return 0, 0  

def display_incorrect_guesses(incorrect_guesses):
    return f'{Fore.RED}Incorrect guesses: {Style.BRIGHT}' + ' '.join(incorrect_guesses)  # Letras incorrectas en rojo

# Resto del código...

def hangman():
    welcome()
    wins, losses = load_stats()
    while True:
        word_to_guess = get_valid_word(palabras)
        word_letters = set(word_to_guess)
        alphabet = set(string.ascii_uppercase)
        guessed_letters = set()
        incorrect_guesses = set()
        lives = 6

        while lives > 0:
            print(hangmanASCI[lives])

            current_display = display_word(word_to_guess, guessed_letters)
            print(current_display)
            print(display_incorrect_guesses(incorrect_guesses))

            guess = input("Guess a letter: ").upper()

            if guess in alphabet - guessed_letters:
                guessed_letters.add(guess)
                if guess not in word_letters:
                    lives -= 1
                    incorrect_guesses.add(guess)

                if set(word_letters).issubset(guessed_letters):
                    print(hangmanASCI[lives])
                    print(f'{Fore.GREEN}Congratulations! You guessed the word: {word_to_guess}')
                    wins += 1
                    break
            elif guess in guessed_letters:
                print(f'{Fore.YELLOW}You have already guessed that letter, try again.')  # Mensaje en amarillo
            else:
                print(f'{Fore.RED}Invalid input. Please enter a valid letter.')  # Mensaje en rojo

            print(f'Lives left: {Style.BRIGHT}{Fore.CYAN}{lives}')  # Vidas restantes en cyan

        if lives == 0:
            print(hangmanASCI[lives])
            print(f'{Fore.RED}Sorry, you ran out of lives. The word was: {word_to_guess}')

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman()