print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What % tip do you want to give? "))
people = int(input("How many people will split the bill? "))

res = (bill * (1+tip/100)) / people

roundedRes = round(res, 2)

print("Each person should pay: $" + str(roundedRes))