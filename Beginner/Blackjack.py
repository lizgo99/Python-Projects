import os
import random
from art import blackjack_logo as logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def is_blackjack(cards):
  if 11 in cards and 10 in cards and len(cards) == 2:
    return True
  else:
    return False
  
def calculate_score(cards):
  #replace 11 with 1, if exists
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  while cards.count(11) > 0 and sum(cards) > 21:
    for card in cards:
      if card == 11:
        cards.remove(card)
        cards.append(1)
  return sum(cards)

def winner(players_score,dealers_score):
  if players_score > 21: 
    return "You went over. You Lose"
  elif dealers_score > 21: 
    return "Dealer went over. You win"
  elif dealers_score == players_score: 
    return "It's a draw"
  elif players_score == 0: 
    return "Win with a Blackjack"
  elif dealers_score == 0: 
    return "Lose, opponent has Blackjack"
  elif dealers_score > players_score: 
    return "You lose"
  elif dealers_score < players_score: 
    return "You win"
  
  
def blackjack():
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    players_cards = [deal_card(), deal_card()]
    dealers_cards = [deal_card(), deal_card()]
    should_continue = True
    while should_continue:
      players_score = calculate_score(players_cards)
      dealers_score = calculate_score(dealers_cards)
      print(f"  Your cards: {players_cards}, current score: {players_score}")
      print(f"  Dealer's first card: {dealers_cards[0]}")
      if is_blackjack(players_cards) or is_blackjack(dealers_cards) or players_score > 21 or dealers_score > 21:
        should_continue = False
      else:
        cont = input("Type 'y' to get another card, type 'n' to pass: ")
        if cont == 'y':
          players_cards.append(deal_card())
        elif cont == "n":
          should_continue = False

    while dealers_score < 17:
      new_dealer_card = deal_card()
      dealers_cards.append(new_dealer_card)
      dealers_score += new_dealer_card
      
    print(f"  Your final hand: {players_cards}, final score: {players_score}")
    print(f"  Dealer's final hand: {dealers_cards}, final score: {dealers_score}")
    print(winner(players_score,dealers_score))
    blackjack()  
      
blackjack()
