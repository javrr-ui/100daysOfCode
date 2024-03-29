from art import logo
import random
from os import system

def clear():
    _ = system("cls")

def print_ui():
    clear()
    print(logo)
    print("I'm thinking of a number between 1 and 100")
def play_game():
    random_number = random.randint(0,100)
    
    #clear console before starting the game
    clear()
    #print(random_number)
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
        
        print_ui()
        while attempts > 0:
            
            print(f"You have {attempts} attempts left to guess the number.")
            user_answer = int(input("Make a guess: "))
            
            if user_answer == random_number:
                print_ui()
                print(f"You got it! The answer was {random_number}")
                break
            elif user_answer < random_number:
                print_ui()
                print(f"{user_answer} is too low.")
                if attempts == 1:
                    print("You lose")
                attempts -= 1
            elif user_answer > random_number:
                print_ui()
                print(f"{user_answer} is too high.")
                if attempts == 1:
                    print("You lose")
                attempts -= 1

        play_again = input("Do you want to play again?: ")
        if play_again == "yes":
            play_game()
        
play_game()