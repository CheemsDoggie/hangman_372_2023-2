# HANGMAN_372_2023-2 WITH PYTHON 🐍🧍‍♂️

> Programacion con Python. Ejercicio colaborativo Pull Request (PR) para examen ordinario 2023-2 grupo 372.
>
> Hangman build with python language

## Descripción del Proyecto
El clásico juego del ahorcado desarrollado en Python. Este proyecto es un esfuerzo colaborativo para implementar el juego con funcionalidades básicas, proporcionando una experiencia divertida y educativa.

---
## STEPS:
1. Welcome
2. Generate a list of words
3. Choose/select a word from the list (or data bank X)
4. Dicard word in case it contains '-' or ' '
5. Convert word to uppercase
6. Split the word in letters
7. Ask the user letter to guess the word.
8. Save and compare the requested letters.
   - Save if guess
   - Take a life if not guessed
9.  Remove letters from the split word
10. If the user removed all the letters he won otherwise not
---
Improvements:

1.  Print the man's ascii art
2.  Improve README.md


# Cambios - Bojorges Eddy

Realice cambios en el main.py agregando el 6 - lives para que este imprimiera 
correctamente los hangman y quite los ; que estaban en los mismo. 

```python
print(hangmanASCI[ 6 - lives])
```
Ademas modifique el archivo resources.py, de la parte de los hangman. Nada que destacar.

### Agregado de Estadisticas

Agregue una funcion llamada load_stats para cargar estadísticas desde stats.txt y si no tiene datos
devuelve los datos 0, 0.
```python
# Función para cargar estadísticas desde un archivo
def load_stats():
    try:
        with open("stats.txt", "r") as file:
            stats = file.readlines()  
            wins, losses = map(int, stats)  
            return wins, losses  
    except FileNotFoundError:  
        return 0, 0  

```

Funcion save_stats para guardar las veces que se ha ganado y perdido en el
archivo en donde file.write escribe las estadisticas en el archivo.
```python
# Función para guardar estadísticas en un archivo
def save_stats(wins, losses):
    with open("stats.txt", "w") as file:
        file.write(f"{wins}\n{losses}")  

```

Funcion display_stats muestra las estadisticas en pantalla cuando se gana o se pierde
```python
#función para mostrar estadísticas en la consola
def display_stats(wins, losses):
    print(f"Wins: {wins} | Losses: {losses}") 

```

Imprime en pantalla las veces que se perdio y se gano
```python
 display_stats(wins, losses)
```

Agregado de while para repetir el juego mientras el usuario lo quiera
```python
 #While para seguir jugando si el jugador asi lo quiere
    while True:
        word_to_guess = get_valid_word(palabras)
        word_letters = set(word_to_guess)
        alphabet = set(string.ascii_uppercase)
        guessed_letters = set()
        incorrect_guesses = set()
        lives = 6
```
En esta parte se le pregunta al usuario si quiere seguir jugando, tranforma lo ingresado a mayusculas y si es diferente de YES se acaba y se guardan los datos y se hace un break para detener el juego
```python
play_again = input("Do you want to play again? (yes/no): ").upper()
   if play_again != "YES":
      save_stats(wins, losses)
      break
```


# Escobedo Jonathan

Esta funcion detecta cuando se equivoca 2 veces y revela una letra en modo de pista.

```python
def reveal_letter(word_letters, guessed_letters, incorrect_guesses):
    incorrect_count = len(incorrect_guesses)
    if incorrect_count >= 2:
        for letter in word_letters:
            if letter not in guessed_letters:
                return letter
    return None

```

aqui se detecta atravez de un IF cuando el jugador se equivoca 2 veces y ejecuta la funcion.

```python
 letter_to_reveal = reveal_letter(word_letters, guessed_letters, incorrect_guesses)
                if letter_to_reveal:
                    print(f"Oops! You've made 2 incorrect guesses. Here's a letter: {letter_to_reveal}")
                    guessed_letters.add(letter_to_reveal)
```