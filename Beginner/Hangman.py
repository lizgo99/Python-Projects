import os
from Hangman_words import word_list
from Hangman_art import logo, stages

# chosen_word = random.choice(word_list)
chosen_word = "math"
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
  
guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if guess in guessed_letters:
        print("You have already guessed this letter. Try again")
    else:
      guessed_letters.append(guess)
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")
              print(f"The word was: {chosen_word}")
  
      print(f"{' '.join(display)}")
  
      if "_" not in display:
          end_of_game = True
          print("You win.")
  
      print(stages[lives])