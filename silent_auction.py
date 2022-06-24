""" The programs takes anonymous bids from bidders as input, 
clear the screen for the next bidder and the return the highest bidder.
"""

auction = """
                             __
  .--------------.___________) \  
 |//////////////|___________[ ]   
  `--------------'           ) (      
                             '-'   
"""

import os

print(auction)

# clear the screen for the next bider
def clear_screen():
    # check if the operating system is Mac and Linux or Windows
   if os.name == "nt":
      os.system("cls")
   else:
      os.system("clear")

# store users' names and bids
bids = {}

# to check if input entered for bid is an integer 
is_bid_input_valid = False

# to check if there are other bidders
is_bid_finished = False

# the function takes all bids and return the highest bid
def highest_bidder(all_bidders):
  highest_bid = 0
  bidding_winner = ""
  for bidder in all_bidders:
    bid = all_bidders[bidder]
    if bid > highest_bid: 
      highest_bid = bid
      bidding_winner = bidder
  clear_screen()
  print(auction)
  print(f"The winner is {bidding_winner} with a bid of ${highest_bid}")

# check for other bidders and input validity
while not is_bid_finished and not is_bid_input_valid: 
  # loop until the user enters a valid integer
  input_name = input("What is your name?: ")
  try: 
    input_bid = int(input("What is your bid?: $ "))
    is_bid_input_valid = True # if this point is reached, a valid integer was entered for the bid

    bids[input_name] = input_bid
    other_biders = input("Are there any other biders? Type 'yes' or 'no' ")
    if other_biders == "no":
      is_bid_finished = True
      highest_bidder(bids)
    elif other_biders == "yes":
      clear_screen()
      print(auction)
      is_bid_finished = False
      is_bid_input_valid = False
  
  except ValueError:
      print("Please only input digits")
      
# use this link to place your bid: https://replit.com/@lydiecherilus/silentauction?v=1
