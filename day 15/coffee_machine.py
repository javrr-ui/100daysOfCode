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


def make_coffee(type):
    if type == "espresso":
        # make espresso
        pass
    elif type == "latte":
        # make latte
        pass
    elif type == "cappuccino":
        # make cappuccino
        pass


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def run():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.

# TODO: 3. Print report.

# TODO: 4. Check resources sufficient?

# TODO: 5. Process coins.

# TODO: 6. Check transaction successful?

# TODO: 7. Make Coffee.

run()
