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

player_cards = []
cpu_cards = []
player_score = 0
cpu_score = 0

def clear():
    _ = system("cls")

def print_cards():
    print(f"Your cards: {player_cards}, current score is {player_score}")

def draw_card(player_name, count):
    for i in range(count):
        players[player_name].get("cards").append(choice(cards))
    
def play():
    global player_score
    global cpu_score
    if not input('Do you want to play a game of Blackjack? Type "y" or "n": ').lower() == "y":
        clear()
        play()

    print(logo)
    draw_card(name="player",count=2)
 
    for value in player_cards:
        player_score += value

    draw_card(name="cpu",count=2)

    for value in cpu_cards:
        cpu_score += value 

    print_cards()

    draw_again  = True
    while draw_again:
       
        print(f"Computer first card: {cpu_cards[0]}")
        if input('Type "y" to get another card, type "n" to pass: ').lower() == "y":
            card = choice(cards)
            player_cards.append(card)
            player_score += card
            print_cards()
        else:
            break

        if player_score > 21:
            break
    
    if cpu_score <= 16:
        card = choice(cards)
        cpu_cards.append(card)
        cpu_score += card
        while True:
            if cpu_score > 16 and cpu_score <= 21:
                break
            if cpu_score <= 16:
                card = choice(cards)
                cpu_cards.append(card)
                cpu_score += card
            if cpu_score > 21:
                break

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computers final hand: {cpu_cards}, final score: {cpu_score}")

clear()
play()