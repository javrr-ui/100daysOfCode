from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


def run():
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        print("Coffee machine is now turned Off")
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
        run()
    else:
        drink = menu.find_drink(choice)
        if drink:
            # Check resources
            if coffee_machine.is_resource_sufficient(drink):
                print(f"Your {drink.name} is ${drink.cost}")
                payment_is_valid = money_machine.make_payment(drink.cost)
                if payment_is_valid:
                    coffee_machine.make_coffee(drink)
        run()


run()
