import random
import os
clear = lambda: os.system('cls')
 
clear()
 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 
def blackjack():
  myCards= []
  cpuCards= []
 
  sumMyCards = 0
  sumCpuCards = 0
 
  for i in range(2):
    myCards.append(random.choice(cards))
    cpuCards.append(random.choice(cards))
 
    sumMyCards += myCards[i]
    sumCpuCards += cpuCards[i]
 
  print(f"  Your cards: {myCards}, current score: {sumMyCards}")
  print(f"  Computer's first card: {cpuCards[0]}\n")
 
  moreCards = input("Type 'y' to get another card, type 'n' to pass: ")
 
  if moreCards == 'y':
    gameOver = False
  elif moreCards == 'n':
    gameOver = True
 
  while not gameOver:
    i += 1
    myCards.append(random.choice(cards))
    sumMyCards += myCards[i]
 
    print(f"  Your cards: {myCards}, current score: {sumMyCards}")
    print(f"  Computer's first card: {cpuCards[0]}\n")  
 
    if sumMyCards > 21:
      break
 
    moreCards = input("Type 'y' to get another card, type 'n' to pass: ")
 
    if moreCards == 'y':
      gameOver = False
    elif moreCards == 'n':
      gameOver = True
 
  print(f"  Your final hand: {myCards}, final score: {sumMyCards}")
  print(f"  Computer's final hand: {cpuCards}, final score: {sumCpuCards}\n")
 
  myScore = 21 - sumMyCards
  cpuScore = 21 - sumCpuCards
 
  if myScore < cpuScore and myScore>=0:
    print("You win!")
  elif myScore > cpuScore and myScore>=0:
    print("You lost...")
  elif myScore == cpuScore and myScore>=0:
    print("Draw.")
  else:
    print("You went over. You lose")
 
  again = input("Do you want to play a game of Blackjack? Type 'y' ou 'n': ")
 
  if again == 'y':
    clear()
    blackjack()
  elif again == 'n':
    print("See you soon ;)")
 
 
again = input("Do you want to play a game of Blackjack? Type 'y' ou 'n': ")
 
if again == 'y':
  clear()
  blackjack()
elif again == 'n':
  print("See you soon ;)")