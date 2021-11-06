import math

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
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def make_coffee(coffee_type):
    if coffee_type == "espresso":
        # make espresso
        pass
    elif coffee_type == "latte":
        # make latte
        pass
    elif coffee_type == "cappuccino":
        # make cappuccino
        pass


# TODO: 3. Print report.
def print_report():
    print("---- Resource report ----")
    for ingredient in resources:
        ingredient_quantity = str(resources[ingredient])
        if ingredient == "water" or ingredient == "milk":
            ingredient_quantity += "ml"
        else:
            ingredient_quantity += "gr"
        print(f"{ingredient.capitalize()}: {ingredient_quantity} ")
    print("-------------------------")


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def run():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off the coffee machine by entering "off"
    if user_input == "off":
        print("Coffee Machine is now turned Off.")
    elif user_input == "report":
        print_report()
    # If coffee name is in the MENU, then prepare it
    elif user_input in MENU.keys():
        # Check resources
        missing_resources = check_resources(user_input)
        if missing_resources:
            print(f"There's not enough of the following ingredients: {missing_resources}")
        else:
            # make coffee
            process_payment(user_input)
            make_coffee(user_input)
            print(f"Making your {user_input} ☕")
    else:
        print("That's not a valid option!")


# TODO: 4. Check resources sufficient?
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


# TODO: 5. Process coins.
def process_payment(coffee_type):
    # Show coffee price
    coffee_price = MENU[coffee_type]["cost"]
    print(f"Your {coffee_type} is ${coffee_price}")
    print("Please insert coins.")
    payment = 0
    for coin in coins:
        print("your bank is: ${0:.2f}".format(payment))
        user_coins = float(input(f"How many {coin}?"))
        payment += user_coins * coins[coin]
    print("your bank is: ${0:.2f}".format(payment))


# TODO: 6. Check transaction successful?

# TODO: 7. Make Coffee.

run()
