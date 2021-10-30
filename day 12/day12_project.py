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
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ').lower()
    if not difficulty == "easy" and not difficulty == "hard":
        input("That's not a valid option, please try again\nPress Enter to continue")
        play_game()

    if difficulty == "easy":
        attempts = 10
    if difficulty == "hard":
        attempts = 5

play_game()