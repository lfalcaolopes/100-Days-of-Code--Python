import random

wordList = ["aloha", "papagaio", "naruto", "tiktok", "bruxa"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
blankList = []
gameOverCounter = 1
playersLife = 6



chosenWord = wordList[random.randint(0, len(wordList)-1)]

print(chosenWord)

for i in range(len(chosenWord)):
  blankList.append("_")
blankSpaces = " ".join(blankList)

while gameOverCounter!=0 and playersLife!=0:
  test = 0
  gameOverCounter = 0

  playersGuess = input("Choose a letter: ").lower()

  for i in range(len(chosenWord)):
    if playersGuess == chosenWord[i]:
      blankList[i] = playersGuess
      test = 1
    
    if blankList[i]=="_":
      gameOverCounter += 1

  blankSpaces = " ".join(blankList)
  print(blankSpaces)

  if test==0:
    print(f"You guessed {playersGuess}, that's not in the word. You lose a life")
    playersLife -= 1

  if playersLife == 6:
    print(stages[6])
  elif playersLife == 5:
    print(stages[5])
  elif playersLife == 4:
    print(stages[4])
  elif playersLife == 3:
    print(stages[3])
  elif playersLife == 2:
    print(stages[2])
  elif playersLife == 1:
    print(stages[1])
  elif playersLife == 0:
    print(stages[0])


if gameOverCounter == 0:
  print("\nYou Won!\n")
elif playersLife == 0:
  print("\njezz u trash...\n")