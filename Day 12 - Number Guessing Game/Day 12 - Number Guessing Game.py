import random

print("Welcome to the Numer Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def defineNumber():
  number = random.randint(0, 100)

  return number

def playersLife():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  if difficulty == "easy":
    return 10
  elif difficulty=="hard":
    return 5

def playersGuess():
  chute = int(input("Make a guess: "))

  return chute

def checkGuess(guess,randomNumber):
  if guess > randomNumber:
    return "Too High\n"
  elif guess < randomNumber:
    return "Too Low\n"
  elif guess == randomNumber:
    return f"You got it! The answer was {randomNumber}"

def game():
  lifeAmount = playersLife()

  randomNumber = defineNumber()

  counter = 0

  for attempts in range(lifeAmount):
    print(f"You have {lifeAmount - attempts} attempts remaining to guess the number.")

    guess = playersGuess()

    cGuess = checkGuess(guess, randomNumber)

    print(cGuess)

    if guess == randomNumber:
      counter = 1
      break

  if counter == 0:
    print("You've run out of guesses, you lose")

game()