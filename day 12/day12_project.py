from art import logo
import random
from os import system

def clear():
    _ = system("cls")

def play_game():
    random_number = random.randint(0,100)
    
    #clear console before starting the game
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
    if not difficulty == "easy" or not difficulty == "hard":
        input("That's not a valid option, please try again\nPress Enter to continue")
        play_game()

play_game()