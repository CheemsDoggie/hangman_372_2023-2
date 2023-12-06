import random
from resources import palabras
from resources import hangmanASCI

def welcome():
    print("Welcome to the hangman game in Python")

def get_valid_word(words):                                  
    word = random.choice(words)
    if word.isalpha:                    # evalua si la palabra de la lista sólo contiene letras
        return word.upper()             # devuelve la palabra en mayúsculas
    else:                               # si no: selecciona otra palabra de la lista
        get_valid_word(words)
        

def display_word(word, guessed_letters):
    display = 'Word to guess: '
    for letter in word:
        if letter in guessed_letters:       # evalúa si la letra está en el set de letras 
            display += letter + ' '         # en ese caso, muestra la letra seguida de un espacio
        else:                               # si no:
            display += '_ '                 # muestra un '_ '
    return display.strip()                  # elimina carracteres que no interesen

def display_incorrect_guesses(incorrect_guesses):
    return 'Letras incorrectas: ' + ' '.join(incorrect_guesses)

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
        word_to_guess = get_valid_word(palabras)            # obtiene una palabra random de resources
        word_letters = set(word_to_guess)                   # set de las letras de la palabra incognita
        guessed_letters = set()                             # creacion de un set de letras adivinadas
        incorrect_guesses = set()                           # creacion de un set de letras no adivinadas
        lives = 6                                           # intentos

        while lives > 0:
            print(hangmanASCI[6 - lives])                                       # imprime el ascii de la lista, usando el index restando del 6(total) las vidas disponibles 
            current_display = display_word(word_to_guess, guessed_letters)
            print(current_display)
            print(display_incorrect_guesses(incorrect_guesses))

            guess = input("Guess a letter: ").upper()

            while not guess.isalpha() or len(guess) != 1:                       # evalua que sea guess contenga el valor de una letra
                print("Invalid input. Please enter a single letter.")
                guess = input("Guess a letter: ").upper()

            if guess not in guessed_letters:                                    # evalua si la letra ya ha sido capturada, si no, se agrega al set de letras capturadas
                guessed_letters.add(guess)
                if guess not in word_letters:                                   # si no es parte de la palabra: resta 1 vida
                    lives -= 1
                    incorrect_guesses.add(guess)                                # agrega la letra a capturas incorrectas
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
        save_stats(wins, losses)
        #Pregunta al usuario si  quiere seguir jugando
        while True:
            try:
                play_again = int(input('Do you want to play again?\n[1] Yes\n[2] No\n'))
                if play_again == 1:
                    hangman()
                elif play_again == 2:
                    exit()
                else:
                    print("Invalid input. Please enter either 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid integer (1 or 2).")

if __name__ == "__main__":
    hangman()