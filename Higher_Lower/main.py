from art import logo
from art import vs
from game_data import data
import random
from replit import clear

print(logo)
score = 0 
count = 0
still_playing = True
character2 = ""
def sort(character1,character2):
  compare = []
  compare.append(character1["follower_count"])
  compare.append(character2["follower_count"])
  return sorted(compare)


while still_playing == True:
  if count >= 1:
    temp = character2
    character1= temp
  else:
    character1 = random.choice(data)
    
  print(f"Your score is {score}")
  print(f"{character1['description']} {character1['name']} has {character1['follower_count']} million followers.")
  character2 = random.choice(data)
  print(vs)
  print(f"{character2['description']} {character2['name']} has higher(h) or lower(l) amount followers")
  user_input = input (": ")
  game = sort(character1,character2)

  if user_input == "higher" or user_input == "h" and game[1] == character2["follower_count"]:
    score+=1
    count +=1
    clear()
  elif user_input == "lower" or user_input == "l" and game[0] == character2["follower_count"]:
    score+=1
    count +=1
    clear()
  else:
    if score > 0 and score <= 3:
      print(f"Terrible score.\nDisgraceful performance\nYou lost. Total score is {score}")
      still_playing = False
    elif score > 3 and score < 7:
      print(f"Average\nTotal score is {score}")
      still_playing = False 
    else:
      print(f"You know your stuff\nTotal score is {score}")
      still_playing = False 

    
    
