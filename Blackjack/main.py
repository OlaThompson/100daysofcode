from art import logo
import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_name = input("Player name: ")
game_bid = 1000
details = {
  game_name : game_bid
  }
quit = True
user_hand = []
computer_hand = []

def hit():
  return random.choice(cards)

def calculated_score():
  for card in user_hand:
    sum(card)
  print(f"Your total hand is {sum(card)}")
  for card in computer_hand:
    sum(card)
  print(f"Your total hand is {sum(card)}")
  

                       
while game_bid >0:
  print(details)
  print(f"You have {details[game_name]} left")
  user_deal = int(input("To start game, place deal greater than 100 \n:"))
  game_bid -= user_deal
  print("First deck")
  user_hand = user_hand.append(hit())
  print(user_hand)
  computer_hand = computer_hand.append(hit())
  print("Second deck")
  user_hand = user_hand.append(hit())
  print(user_hand)
  computer_hand = computer_hand.append(hit())
  print(f"Your cards {user_hand} and computer card [{computer_hand[0]},_]")
  next_stage = input("Do you want to split (Y/N)").lower()
  if next_stage == "y":
    game_bid -= user_deal
    print(details)
    user_hand.pop()
    user_hand = user_hand.append(hit())
    print(user_hand)

  else:
    print ("Take a hit or stand")
    
  
  if next_stage == "hit":
    user_hand = user_hand.append(hit())
    print(user_hand)
    computer_hand = computer_hand.append(hit())
    calculated_score()
  elif next_stage == "split":
    game_bid -= user_deal
    print(details)
    user_hand.pop()
    user_hand = user_hand.append(hit())
    print(user_hand)
  elif next_stage == "stand"
    
    
                     
  

    
    
  
  
  
  

