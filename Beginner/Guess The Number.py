
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import guess_logo as logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  elif level == "hard":
    return HARD_LEVEL_TURNS

def check_guess(guess,answer,num_of_guesses):
  if guess < answer:
    print("Too low.")
    return num_of_guesses - 1
  elif guess > answer:
    print("Too high.")
    return num_of_guesses - 1
  else:
    print(f"You got it! The answer was {answer}.")
    
def game(): 
  print(logo)
  print("Welcom to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = random.randint(1,100)
#   print(f"Pssst, the correct answer is {answer}")
  level = set_level()
  guess = 0
  while guess != answer:
    print(f"You have {level} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    level = check_guess(guess, answer, level)
    
    if level == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
  
game()