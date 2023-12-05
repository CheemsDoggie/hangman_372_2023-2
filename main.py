import random
import string
from resources import palabras
from resources import hangmanASCI

def welcome():
    print("Welcome to the hangman game in Python")

def get_game_mode(): #pregunta que modo de juego quiere jugar
    while True:
        mode = input("Choose game mode - 'random' for a random word or 'custom' to enter a word: ").lower()
        if mode in ["random", "custom"]:
            return mode
        else:
            print("Invalid input. Please type 'random' or 'custom'.")

def get_valid_word(words, mode):
    if mode == "random":
        word = random.choice(words)
        while '-' in word or ' ' in word:
            word = random.choice(words)
        return word.upper()
    else:
        while True:
            word = input("Enter a word for someone else to guess: ")
            if "-" in word or " " in word or not word.isalpha():
                print("Invalid word. Please enter a word without spaces or hyphens.")
            else:
                return word.upper()

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
    mode = get_game_mode()
    wins, losses, total_attempts, total_games = load_stats()
    while True:
        word_to_guess = get_valid_word(palabras, mode)
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

        # Pregunta al usuario si quiere seguir jugando o cambiar de modo
        play_again = input("Do you want to play again (write 'change' to play another game mode)? (yes/no/change): ").lower()
        if play_again == "no":
            save_stats(wins, losses, total_attempts, total_games)
            break
        elif play_again == "change":
            mode = get_game_mode()

if __name__ == "__main__":
    hangman()
