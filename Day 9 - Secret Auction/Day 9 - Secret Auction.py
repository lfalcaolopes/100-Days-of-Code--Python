import os
clear = lambda: os.system('cls')

clear()
print("Welcome to the secret auction program.")

auctionData = []

anyBidders = True
winningBid = 0

while anyBidders:
  name = input("What is your name?: ")
  bidAmount = int(input("What's your bid?: $"))

  auctionData.append({
    "participant" : name,
    "bid" : bidAmount,
  })

  again = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if again == "yes":
    clear()
  elif again =="no":
    anyBidders = False

for data in auctionData:
  if winningBid < data["bid"]:
    winningBid = data["bid"]
    winner = data["participant"]


print(f"The winner is {winner} with a bid of ${winningBid}.")
