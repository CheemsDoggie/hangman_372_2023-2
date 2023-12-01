import random
import string

from resources import palabras
from resources import hangmanASCI

puntos_por_letra = 2

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

# Calculo de puntaje de acuerdo al numero de letras adivinadas correctamente
def calculate_score(word_to_guess, guessed_letters):
    return sum(puntos_por_letra for letter in guessed_letters if letter in word_to_guess)

# Ordena y muestra los 5 mejores puntajes encontrados
def get_top_scores():
    try:
        with open("scores.txt", "r") as file:
            scores = [line.strip().split(":") for line in file]
            scores = [(name, int(score)) for name, score in scores]
            scores.sort(key=lambda x: x[1], reverse=True)
            return scores[:5]
    except FileNotFoundError:
        return []

# Guarda el puntaje en el archivo scores
def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name}:{score}\n")

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

    # Calcular y mostrar puntos
    score = calculate_score(word_to_guess, guessed_letters)
    print("Your score:", score)

    # Pedir el nombre del jugador
    player_name = input("Enter your name: ")

    # Guardar el nombre del jugador y su puntaje
    save_score(player_name, score)

    # Mostrar los mejores puntajes
    top_scores = get_top_scores()
    print("\nTop 5 Scores:")
    for i, (name, score) in enumerate(top_scores, start=1):
        print(f"{i}. {name}: {score} points")

if __name__ == "__main__":
    hangman()
