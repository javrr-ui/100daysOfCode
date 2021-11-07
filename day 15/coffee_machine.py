import math
from os import system

MENU = {
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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def clear():
    _ = system("cls")


def press_enter():
    input("Press Enter to continue...")


def make_coffee(coffee_type):
    # Iterate over each ingredient required for the coffee, and subtract to resources
    for ingredient in MENU[coffee_type]["ingredients"]:
        resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]


def print_report():
    print("---- Resource report ----")
    for ingredient in resources:
        ingredient_quantity = str(resources[ingredient])
        if ingredient == "water" or ingredient == "milk":
            ingredient_quantity += "ml"
        elif ingredient == "coffee":
            ingredient_quantity += "gr"
        else:
            ingredient_quantity = "${0:.2f}".format(float(ingredient_quantity))
        print(f"{ingredient.capitalize()}: {ingredient_quantity} ")
    print("-------------------------")
    press_enter()
    clear()


def string_beautify(ingredient_list):
    """Receives a list of ingredients, returns a formatted string of ingredients"""
    ingredient_string = ""
    if len(ingredient_list) > 2:
        ingredient_string = "".join(ingredient_list)
        for ingredient in range(len(ingredient_list)-1):
            ingredient_string = ingredient_string.replace(ingredient_list[ingredient], ingredient_list[ingredient]+", ")
        ingredient_string = ingredient_string.replace(ingredient_list[-1], "and "+ingredient_list[-1])

    elif len(ingredient_list) > 1:
        ingredient_list.insert(-1, " and ")
        for string in ingredient_list:
            ingredient_string += string
    else:
        ingredient_string = ingredient_list[0]

    return ingredient_string


def run():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off the coffee machine by entering "off"
    if user_input == "off":
        print("Coffee Machine is now turned Off.")
    elif user_input == "report":
        clear()
        print_report()
        run()
    # If coffee name is in the MENU, then prepare it
    elif user_input in MENU.keys():
        # Check resources
        missing_resources = check_resources(user_input)
        if missing_resources:
            ingredient_string = string_beautify(missing_resources)
            clear()
            print(f"Sorry, there's not enough {ingredient_string} to make your {user_input} 😢")
            run()
        else:
            # Check if payment is OK
            clear()
            payment_is_valid = process_payment(user_input)
            if payment_is_valid:
                # make coffee
                make_coffee(user_input)
                print(f"Here is your {user_input}, enjoy! ☕")
            else:
                print("Sorry, that's not enough money, please try again.")
            press_enter()
            clear()
            run()
    else:

        print("That's not a valid option!")
        press_enter()
        clear()
        run()


def check_resources(coffee_type):
    """Returns an empty list if resources are sufficient, otherwise returns a list with
    ingredients with insufficient quantity
    """
    # List used to store ingredients with not enough quantity
    ingredient_list = []
    coffee = MENU[coffee_type]
    for ingredient in coffee["ingredients"]:
        # Check if there's enough ingredient quantity to prepare the coffee, if not, add to list
        if not resources[ingredient] >= coffee["ingredients"][ingredient]:
            ingredient_list.append(ingredient)
    return ingredient_list


def process_payment(coffee_type):
    """Checks if user payment is equal or greater than coffee price, returns True of False"""
    # Show coffee price
    coffee_price = MENU[coffee_type]["cost"]

    payment = 0
    for coin in coins:
        clear()
        print(f"Your {coffee_type} is ${coffee_price}")
        print("Please insert coins.")
        print("Your bank is: ${0:.2f}".format(payment))
        user_coins = float(input(f"How many {coin}?: "))
        payment += user_coins * coins[coin]
    clear()
    print("Your bank is: ${0:.2f}".format(payment))

    if math.isclose(payment, coffee_price):
        # Add payment to machine bank
        resources["money"] += payment
        return True
    elif payment > coffee_price:
        # Return change to user
        resources["money"] += coffee_price
        change = payment - coffee_price
        print("Your change is: ${0:.2f}".format(change))
        return True
    else:
        return False


clear()
run()
