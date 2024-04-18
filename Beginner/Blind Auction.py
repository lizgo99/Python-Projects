import os
from art import blind_auction_logo as logo

print(logo)
done = False
bids = {}
while not done:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: "))
  bids[name] = bid
  more_players = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if more_players == "no":
    done = True
    os.system('cls' if os.name == 'nt' else 'clear')
  elif more_players == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')
      
if done:
  max_bid = -1
  max_bidder = ""
  for bidder in bids:
    current_bid = bids[bidder]
    if current_bid > max_bid:
      max_bid = current_bid
      max_bidder = bidder
  print(f"The winner is {max_bidder} with a bid of ${max_bid}")
