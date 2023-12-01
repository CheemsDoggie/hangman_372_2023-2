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


# Cambios
### Bojorges Eddy

Realice cambios en el main.py agregando el 6 - lives para que este imprimiera 
correctamente los hangman y quite los ; que estaban en los mismo. 

```python
print(hangmanASCI[ 6 - lives])
```
Ademas modifique el archivo resources.py, de la parte de los hangman. Nada que destacar.