from art import logo
from art import vs

from game_data import data
from random import choice
from os import system

def clear():
    _ = system("cls")

def get_data():
    return choice(data)
    
def game():
    clear()
    print(logo)

game()