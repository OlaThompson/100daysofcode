import random
from art import logo
print(logo)
print("Guess number from 1 to 100")


print ("Whats your decision")
user_choice = input ("Do you want the Easy mode or Hard mode \n: ").lower()
if user_choice == "easy":
  attempts = 10
else:
  attempts = 5

chosen_number = random.randint(1, 100)
correct = False
while correct == False and attempts > 0 :
  user_guess = int(input("What is your guess?\n:"))
  if user_guess > chosen_number:
    print(f"This is wrong! The number is lower than {user_guess}")
    attempts -= 1
  elif user_guess < chosen_number:
    print(f"This is wrong! The number is higher than {user_guess}")
    attempts -= 1
  else:
    print(f"You guessed correctly")
    correct = True
  
