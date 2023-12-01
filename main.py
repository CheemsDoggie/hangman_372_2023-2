import random
import string
from resources import palabras
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static')

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
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
    return 'Incorrect guesses: ' + ' '.join(incorrect_guesses)
  
# Definir una variable global para almacenar el estado del juego
game_state = None

@app.route('/')
def hangman():
    global game_state

    if game_state is None:
        # Iniciar un nuevo juego
        word_to_guess = get_valid_word(palabras)
        word_letters = set(word_to_guess)
        game_state = {
            'word_to_guess': word_to_guess,
            'word_letters': word_letters,
            'alphabet': set(string.ascii_uppercase),
            'guessed_letters': set(),
            'incorrect_guesses': set(),
            'lives': 6,
            'wins': 0,
            'losses': 0
        }

    # Obtener el estado actual del juego
    current_display = display_word(game_state['word_to_guess'], game_state['guessed_letters'])
    incorrect_guesses_display = display_incorrect_guesses(game_state['incorrect_guesses'])

    return render_template('hangman.html', game_state=game_state, display=current_display, incorrect_guesses=incorrect_guesses_display, result=None)

@app.route('/guess', methods=['POST'])
def guess_letter():
    global game_state

    if game_state is None:
        return "Game not started"

    # Obtener la letra adivinada del formulario
    guess = request.form.get('letter').upper()

    # Realizar la lógica de adivinanza aquí
    if guess in game_state['alphabet'] - game_state['guessed_letters']:
        game_state['guessed_letters'].add(guess)
        if guess not in game_state['word_letters']:
            game_state['lives'] -= 1
            game_state['incorrect_guesses'].add(guess)

    if set(game_state['word_letters']).issubset(game_state['guessed_letters']):
        game_state['wins'] += 1
        result = "Congratulations! You guessed the word: " + game_state['word_to_guess']
        restart_game()
        return redirect(url_for('hangman', result=result))

    elif guess in game_state['guessed_letters']:
        result = "You have already guessed that letter, try again."
        return redirect(url_for('hangman', result=result))

    elif guess not in game_state['alphabet']:
        result = "Invalid input. Please enter a valid letter."
        return redirect(url_for('hangman', result=result))

    if game_state['lives'] == 0:
        game_state['losses'] += 1
        result = "Sorry, you ran out of lives. The word was: " + game_state['word_to_guess']
        restart_game()
        return redirect(url_for('hangman', result=result))

    return redirect(url_for('hangman'))

@app.route('/restart')
def restart_game():
    global game_state
    game_state = None
    return redirect(url_for('hangman'))

if __name__ == '__main__':
    app.run(debug=True)
=======
# Función para cargar estadísticas desde un archivo
def load_stats():
    try:
        with open("stats.txt", "r") as file:
            stats = file.readlines()  
            wins, losses = map(int, stats)  
            return wins, losses  
    except FileNotFoundError:  
        return 0, 0  


# Función para guardar estadísticas en un archivo
def save_stats(wins, losses):
    with open("stats.txt", "w") as file:
        file.write(f"{wins}\n{losses}")  

# Función para mostrar estadísticas en la consola
def display_stats(wins, losses):
    print(f"Wins: {wins} | Losses: {losses}")  # Muestra las estadísticas de victorias y derrotas

def hangman():
    welcome()
    wins, losses = load_stats()
    #While para seguir jugando si el jugador asi lo quiere
    while True:
        word_to_guess = get_valid_word(palabras)
        word_letters = set(word_to_guess)
        alphabet = set(string.ascii_uppercase)
        guessed_letters = set()
        incorrect_guesses = set()
        lives = 6

        while lives > 0:
            print(hangmanASCI[6 - lives])

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

        display_stats(wins, losses)

        #Pregunta al usuario si  quiere seguir jugand
        play_again = input("Do you want to play again? (yes/no): ").upper()
        if play_again != "YES":
            save_stats(wins, losses)
            break

if __name__ == "__main__":
    hangman()
