from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()

coffee = CoffeeMaker()

money = MoneyMachine()


def coffee_machine():
    on_off = True

    while on_off:
        order = input(f"What would you like? ({menu.get_items()}): ")

        if order == 'off':
            on_off = False
        elif order == 'report':
            coffee.report()
            money.report()
        else:
            menu_item = menu.find_drink(order)

            if coffee.is_resource_sufficient(menu_item) and money.make_payment(menu_item.cost):
                coffee.make_coffee(menu_item)


coffee_machine()
