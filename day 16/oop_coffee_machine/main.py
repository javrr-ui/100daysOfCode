from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()


def run():
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        print("Coffee machine is now turned Off")
    elif choice == "report":
        # Print report
        run()
    else:
        drink = menu.find_drink(choice)
        if drink:
            # Check resources
            if coffee_machine.is_resource_sufficient(drink):
                print(f"{drink.name} can be made")
            else:
                print("No")
            pass
        run()


run()
