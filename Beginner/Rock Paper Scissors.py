from art import rock, paper, scissors

import random
print("Let's start!")
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
comp_choice = random.randint(0,2)
if player_choice == "0":
  print(rock)
  if comp_choice == 0:
    print(rock)
    print("It's a tie")
  elif comp_choice == 1:
    print(paper)
    print("You lose 🙁")
  elif comp_choice == 2:
    print(scissors)
    print("YOU WIN! 🎉")
  else:
    print("The computer chose a wrong number")
elif player_choice == "1":
  print(paper)
  if comp_choice == 0:
    print(rock)
    print("YOU WIN! 🎉")
  elif comp_choice == 1:
    print(paper)
    print("It's a tie")
  elif comp_choice == 2:
    print(scissors)
    print("You lose 🙁")
  else:
    print("The computer chose a wrong number")
elif player_choice == "2":
  print(scissors)
  if comp_choice == 0:
    print(rock)
    print("You lose 🙁")
  elif comp_choice == 1:
    print(paper)
    print("YOU WIN! 🎉")
  elif comp_choice == 2:
    print(scissors)
    print("It's a tie")
  else:
    print("The computer chose a wrong number")
else:
  print("You chose something that doesn't exist")
