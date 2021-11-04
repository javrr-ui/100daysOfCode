from art import logo
from art import vs

from game_data import data
from random import choice
from os import system

game_over = False
score = 0

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
    message = f"You're right! Current score: {score}"
    clear()
    print(logo)
    if score > 0 and game_over == False:
        print(message)

    a = get_data()
    b = get_data()
    print(f"Compare A: {data_string(a)} {a['follower_count']}")
    print(vs)
    print(f"Against B: {data_string(b)} {b['follower_count']}")

    user_input = input('Who has more followers? Type "A" or "B": ').lower()
    a_count = a["follower_count"]
    b_count = b["follower_count"]
    if  (a_count > b_count and user_input == "a") or (b_count > a_count and user_input == "b"):
        score += 1
        game()
game()