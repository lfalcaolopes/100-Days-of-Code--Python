menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def recipe(ordering):
    return menu[ordering]['ingredients']


def checking_resources(ordering):
    ingredients = recipe(ordering)
    status = True
    items = 0

    for items in ingredients:
        if ingredients[items] <= resources[items]:
            status = True
        else:
            status = False
            break

    data = {'status': status, 'missing_item': items}

    return data


def processing_coins():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))

    total_money = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01

    return total_money


def processing_order(ordering):
    ingredients = recipe(ordering)

    for items in ingredients:
        resources[items] -= ingredients[items]


def coffee_machine():
    on_off = True

    while on_off:
        order = input("What would you like? (espresso/latte/cappuccino): ")

        if order == 'off':
            on_off = False
        elif order == 'report':
            report()
        elif checking_resources(order)['status']:
            money = processing_coins()
            price = menu[order]['cost']

            if money >= price:
                processing_order(order)

                change = money - price

                resources['money'] += price

                print(f"Here is ${round(change, 2)} in change")

                print(f"Here is your {order}. Enjoy!")
            else:
                print("Insufficient funds. Money refunded.")
        else:
            print(f"Sorry, we are out of {checking_resources(order)['missing_item']}.")


coffee_machine()
