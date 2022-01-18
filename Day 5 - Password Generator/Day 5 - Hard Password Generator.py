import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pLetters = []
pSymbols = []
pNumbers = []
password = []
order = []

for l in range(0, nr_letters):
  pLetters.append(letters[random.randint(0, len(letters)-1)])
  order.append(1)
  
for s in range(0, nr_symbols):
  pSymbols.append(symbols[random.randint(0, len(symbols)-1)])
  order.append(2)

for n in range(0, nr_numbers):
  pNumbers.append(numbers[random.randint(0, len(numbers)-1)])
  order.append(3)

random.shuffle(order)

for i in order:
  if i == 1:
    password.append(pLetters[random.randint(0, len(pLetters)-1)])
  
  elif i == 2:
    password.append(pSymbols[random.randint(0, len(pSymbols)-1)])

  elif i == 3:
    password.append(pNumbers[random.randint(0, len(pNumbers)-1)])

strPassword = ''.join(password)

print(f"Here is your password: {strPassword}")
