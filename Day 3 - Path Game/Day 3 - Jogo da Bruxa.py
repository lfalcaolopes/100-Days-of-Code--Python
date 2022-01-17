print("Welcome to Treasure Island.\nYour mission is to find the treasure")

crossRoad = input("You're at a cross road. Where do you want to go? Type left or right\n")

if crossRoad == "left":
  lake = input("You come to a lake. There is an island in the middle of the lake. Type wait to wait a boat. Type swim to swim across.\n")

  if lake == "wait":
    door = input("You arrive at the island unharmed. there is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    
    if door == "red":
      print("Game Over.")  
    elif door == "yellow":
      print("You Win!")  
    elif door == "blue":
      print("Game Over.")  
  else:
    print("Game Over.")  
else:
  print("Game Over.")  