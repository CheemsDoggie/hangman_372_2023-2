import random
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

# Función para cargar estadísticas desde un archivo
def load_stats():
    try:
        with open("stats.txt", "r") as file:
            stats = file.readlines()
            # Asegúrate de que hay suficientes valores (rellena con 0 si es necesario)
            while len(stats) < 4:
                stats.append("0\n")
            wins, losses, total_attempts, total_games = map(int, stats)
            return wins, losses, total_attempts, total_games
    except FileNotFoundError:
        return 0, 0, 0, 0


# Función para guardar estadísticas en un archivo
def save_stats(wins, losses, total_attempts, total_games):
    with open("stats.txt", "w") as file:
        file.write(f"{wins}\n{losses}\n{total_attempts}\n{total_games}")

# Función para mostrar estadísticas en la consola
def display_stats(wins, losses, total_attempts, total_games):
    average_attempts = total_attempts / total_games if total_games > 0 else 0
    print(f"Wins: {wins} | Losses: {losses} | Average Attempts: {average_attempts:.2f}")

def hangman():
    welcome()
    wins, losses, total_attempts, total_games = load_stats()
    #While para seguir jugando si el jugador asi lo quiere
    while True:
        word_to_guess = get_valid_word(palabras)
        word_letters = set(word_to_guess)
        alphabet = set(string.ascii_uppercase)
        guessed_letters = set()
        incorrect_guesses = set()
        lives = 6
        attempts = 0  # Contador de intentos para este juego

        while lives > 0:
            print(hangmanASCI[6 - lives])

            current_display = display_word(word_to_guess, guessed_letters)
            print(current_display)
            print(display_incorrect_guesses(incorrect_guesses))

            guess = input("Guess a letter: ").upper()
            attempts += 1

            if guess in alphabet - guessed_letters:
                guessed_letters.add(guess)
                if guess not in word_letters:
                    lives -= 1
                    incorrect_guesses.add(guess)

                if set(word_letters).issubset(guessed_letters):
                    print(hangmanASCI[6 - lives])
                    print("Congratulations! You guessed the word:", word_to_guess)
                    wins += 1
                    break
            elif guess in guessed_letters:
                print("You have already guessed that letter, try again.")
            else:
                print("Invalid input. Please enter a valid letter.")

            print("Lives left:", lives)

            if lives == 0:
                print(hangmanASCI[6 - lives])
                print("Sorry, you ran out of lives. The word was:", word_to_guess)
                losses += 1
                break

        total_attempts += attempts
        total_games += 1
        display_stats(wins, losses, total_attempts, total_games)

        #Pregunta al usuario si quiere seguir jugando
        play_again = input("Do you want to play again? (yes/no): ").upper()
        if play_again != "YES":
            save_stats(wins, losses, total_attempts, total_games)
            break

if __name__ == "__main__":
    hangman()
