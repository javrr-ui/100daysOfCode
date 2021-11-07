from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()


def run():
    choice = input(f"What would you like? ({menu.get_items()}): ")
    run()


run()
