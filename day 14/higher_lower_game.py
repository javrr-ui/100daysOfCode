from art import logo
from art import vs

from game_data import data
from random import choice
from os import system

game_over = False

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
    score = 0
    message = f"You're right! Current score: {score}"
    clear()
    print(logo)
    if score > 0 and game_over == False:
        print(message)

    a = get_data()
    b = get_data()
    print(f"Compare A: {data_string(a)}")
    print(vs)
    print(f"Against B: {data_string(b)}")

game()