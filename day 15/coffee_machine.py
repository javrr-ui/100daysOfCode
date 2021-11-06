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


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def run():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    # If coffee name is in the MENU, then prepare it
    if user_input in MENU.keys():
        make_coffee(user_input)
    else:
        print("That's not a valid option!")


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.

# TODO: 3. Print report.

# TODO: 4. Check resources sufficient?
def check_resources(coffee_type):
    # List used to store ingredients with not enough quantity
    ingredient_list = []
    coffee = MENU[coffee_type]
    for ingredient in coffee["ingredients"]:
        # Check if there's enough ingredient quantity to prepare the coffee
        if resources[ingredient] >= coffee["ingredients"][ingredient]:
            print(f"{ingredient}: {coffee['ingredients'][ingredient]} ok")
        else:
            ingredient_list.append(ingredient)
    return ingredient_list


# TODO: 5. Process coins.

# TODO: 6. Check transaction successful?

# TODO: 7. Make Coffee.

run()
print(check_resources("latte"))
