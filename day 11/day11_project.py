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

def calc_score(player_name):
    card_list = players[player_name].get("cards")

    if len(card_list) == 2 and sum(card_list) == 21:
        return 0

    score = 0
    for card in card_list:
        score += card
    players[player_name]["score"] = score
    return score

def draw_card(player_name, count):
    for i in range(count):
        card = choice(cards)
        if card == 11 and calc_score(player_name) + card > 21:
            card = 1
        players[player_name].get("cards").append(card)

    return calc_score(player_name)

def get_score(player_name):
    return players[player_name].get("score")

def get_cards(player_name):
    return players[player_name].get("cards")

def reset_stats():
    for player in players:
        players[player]["cards"] = []
        players[player]["score"] = 0

def play():
    reset_stats()
    if not input('Do you want to play a game of Blackjack? Type "y" or "n": ').lower() == "y":
        clear()
        play()
    clear()
    print(logo)
    player_score = draw_card(player_name="player",count=2)
    cpu_score = draw_card(player_name="cpu",count=2)

    print_cards()

    if cpu_score == 0 and not player_score == 0:
        print("Computer Blackjack, you lose")
    elif not cpu_score == 0 and player_score == 0:
        print("Win with a Blackjack!")
    else:
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

        if get_score("player") == get_score("cpu"):
            print("Draw")
        elif  get_score("player") > get_score("cpu") and get_score("player") <= 21:
            print("You win!")
        elif  get_score("player") < get_score("cpu") and get_score("cpu") <= 21:
            print("You lose!")
        elif get_score("player") <= 21 and get_score("cpu") > 21:
            print("You win!")
        elif get_score("player") > 21 and get_score("cpu") <= 21:
            print("You lose!")
        
    play()

clear()
play()