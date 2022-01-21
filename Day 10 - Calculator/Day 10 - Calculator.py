import os
clear = lambda: os.system('cls')

clear()

sameNumber = True

def add(num1, num2):
  adition = num1 + num2
  return adition

def minus(num1, num2):
  subtraction = num1 - num2
  return subtraction

def times(num1, num2):
  multiplication = num1 * num2
  return multiplication

def divide(num1, num2):
  division = num1 / num2
  return division

operation = {
  '+': add, 
  '-': minus, 
  '*': times, 
  '/': divide,
}

while True:
  num1 = float(input("What's the first number?: "))

  for symbols in operation:
    print(symbols)

  while sameNumber:
    operationSymbols = input("Pick an operation: ")

    num2 = float(input("What's the next number?: "))

    function = operation[operationSymbols]

    result = function(num1,num2)

    print(f"{num1} {operationSymbols} {num2} = {result}")

    num1 = result

    sameNumber = input(f"Type 'y' to continue calculating with {result}, or type 'n' to star a new calculation: ")
    if sameNumber == "y":
      sameNumber = True
    elif sameNumber == "n":
      sameNumber = False
      clear()
