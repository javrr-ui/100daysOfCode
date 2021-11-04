from art import logo
from art import vs

from game_data import data
from random import choice
from os import system

score = 0
a = choice(data)

def clear():
    _ = system("cls")

def get_data():
    return choice(data)

def data_string(dataset):
    """
        Receive a dataset and return a String with formated info
    """
    return f'{dataset["name"]}, a {dataset["description"]}, from {dataset["country"]}'

def game():
    global score
    global a
    message = f"You're right! Current score: {score}"
    clear()
    print(logo)
    if score > 0:
        print(message)

    
    b = get_data()
    while a == b:
        b = get_data()

    print(f"Compare A: {data_string(a)}")
    print(vs)
    print(f"Against B: {data_string(b)}")

    user_input = input('Who has more followers? Type "A" or "B": ').lower()
    a_count = a["follower_count"]
    b_count = b["follower_count"]
    if  (a_count > b_count and user_input == "a") or (b_count > a_count and user_input == "b"):
        score += 1
        a = b
        game()
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        play_again = input('Do you want to play again? Type "Yes" or "No": ').lower()
        if play_again == "yes":
            score = 0
            a = get_data()
            game()
game()