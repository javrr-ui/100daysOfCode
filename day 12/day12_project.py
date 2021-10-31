from art import logo
import random
from os import system

def clear():
    _ = system("cls")

def play_game():
    random_number = random.randint(0,100)
    
    #clear console before starting the game
    clear()
    print(random_number)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ').lower()
    if not difficulty == "easy" and not difficulty == "hard":
        input("That's not a valid option, please try again\nPress Enter to continue")
        play_game()
    else: 
        if difficulty == "easy":
            attempts = 10
        if difficulty == "hard":
            attempts = 5

        print("I'm thinking of a number between 1 and 100")
        print(f"You have {attempts} attempts left to guess the number.")
        user_answer = int(input("Make a guess: "))
        if user_answer == random_number:
            print(f"You got it! The answer was {random_number}")
        elif user_answer < random_number:
            print("Too low.\nGuess again.")
        elif user_answer > random_number:
            print("Too high.\nGuess again.")

play_game()