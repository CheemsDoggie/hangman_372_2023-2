# Import modules to use
from words import palabras
import random
from flask import Flask, render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta básica
@app.route('/')
def hangman():
    return render_template('index.html')

# Punto de entrada para la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)


# 1. Welcome
print("Welcome to the game hangman in Python")

# 2. Function to get word
def get_valid_word(palabras):
  word = random.choice(palabras)

  # Choose a good word
  while '-' in word or ' ' in word: # While - or ' '
    word = random.choice(palabras)

  return word

def hangman():

  word = get_valid_word(palabras) # SOL
  word_letters = set(word) # S, O , L
  alphabet = set(string.ascii_uppercase) # A, B, C, D, E,...
  used_letters = set()
  lives = 6


# Display word and its length
my_word = get_valid_word(palabras)
print(my_word + '\n',len(my_word))


# Una función que despliegue los guiones
# dependiendo el tamaño de la palabra
# Ejemplo:
# A N O N Y M O U S
# _ _ _ _ _ _ _ _ _
print("-"*len(my_word))

