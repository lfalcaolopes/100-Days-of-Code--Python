rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

playersChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if playersChoice == 0:
  print(rock)
elif playersChoice == 1:
  print(paper)
elif playersChoice == 2:
  print(scissors)

print("computer choose:")

computersChoice = random.randint(0, 2)

if computersChoice == 0:
  print(rock)
elif computersChoice == 1:
  print(paper)
elif computersChoice == 2:
  print(scissors)

if playersChoice == computersChoice:
  print("Draw...")
elif playersChoice == 0 and computersChoice == 1:
  print("You Lost.")
elif playersChoice == 0 and computersChoice == 2:
  print("You Win!")
elif playersChoice == 1 and computersChoice == 0:
  print("You Win!")
elif playersChoice == 1 and computersChoice == 2:
  print("You Lost.")
elif playersChoice == 2 and computersChoice == 0:
  print("You Lost.")
elif playersChoice == 2 and computersChoice == 1:
  print("You Win!")
