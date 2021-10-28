############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from os import system
from random import choice
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players = {
    "player": {
        "cards": [],
        "score": 0
    },
    "cpu": {
        "cards": [],
        "score": 0
    }
}

def clear():
    _ = system("cls")

def print_cards():
    cards = players["player"].get("cards")
    score = get_score("player")
    print(f"Your cards: {cards}, current score is {score}")

def draw_card(player_name, count):
    for i in range(count):
        players[player_name].get("cards").append(choice(cards))

    return calc_score(player_name)

def calc_score(player_name):
    card_list = players[player_name].get("cards")

    if len(card_list) == 2 and sum(card_list) == 21:
        return 0

    score = 0
    for card in card_list:
        score += card
    players[player_name]["score"] = score
    return score

def get_score(player_name):
    return players[player_name].get("score")

def get_cards(player_name):
    return players[player_name].get("cards")

def play():
    if not input('Do you want to play a game of Blackjack? Type "y" or "n": ').lower() == "y":
        clear()
        play()

    print(logo)
    player_score = draw_card(player_name="player",count=2)
    cpu_score = draw_card(player_name="cpu",count=2)

    if cpu_score == 0 and not player_score == 0:
        print("Computer Blackjack, you lose")
    elif not cpu_score == 0 and player_score == 0:
        print("Player Blackjack you win!")
    else:

        print_cards()
        while True:
            first_card = players["cpu"].get("cards")[0] 
            print(f"Computer first card: { first_card }")
            if input('Type "y" to get another card, type "n" to pass: ').lower() == "y":
                draw_card("player",count=1)
                
            else:
                break
            if get_score("player") < 21:
                print_cards()

            if get_score("player") >= 21:
                break
        
        
        if get_score("cpu") <= 16:
            draw_card("cpu", 1)
            while True:
                if get_score("cpu") > 16 and get_score("cpu") <= 21:
                    break
                if get_score("cpu") <= 16:
                    draw_card("cpu", 1)
                    continue
                if get_score("cpu") > 21:
                    break

        print(f'Your final hand: {get_cards("player")}, final score: {get_score("player")}')
        print(f'Computers final hand: {get_cards("cpu")}, final score: {get_score("cpu")}')
        
    play()

clear()
play()