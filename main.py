# Import modules to use
from words import palabras
import random

# 1. Welcome
print("Welcome to the game hangman in Python")

# 2. Function to get word
def get_valid_word(palabras):
  word = random.choice(palabras)

  # Choose a good word
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(palabras)

  return word

# Display word and its length
my_word = get_valid_word(palabras)
print(my_word + '\n',len(my_word))


# Una función que despliegue los guiones
# dependiendo el tamaño de la palabra
# Ejemplo:
# A N O N Y M O U S
# _ _ _ _ _ _ _ _ _
print("-"*len(my_word))
