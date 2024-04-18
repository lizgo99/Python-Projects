from art import treasure_island_logo
print(treasure_island_logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

step = input("Your at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if step == "left" or step == "Left":
  lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
  if lake == "wait" or lake == "Wait":
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if door == "blue" or door == "Blue":
      print("Oh no! You got eaten by beasts.\nGame Over")
    elif door == "red" or door == "Red" :
      print("Oh no! It's a room full of fire.\nGame Over")
    elif door == "yellow" or door == "Yellow":
      print("You found the treasure! You Win!")
    else: 
      print("You chose a door that doesn't exist. Game Over")
  else:
    print("Oh no! You got attacked by an angry trout.\nGame Over")
else:
  print("Oh no! You just fell into a hole.\nGame Over")