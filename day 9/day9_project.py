from os import system, name
from art import logo

bidders = {}
run_again = True
def clear():
        _ = system("cls")

def biggest_bid(bidders):
    bid = 0
    name = ""
    for user in bidders:
        if bidders[user] > bid:
            name = user
            bid = bidders[user]
    
    print(f"The winner is {name} with a bid of ${bid}")

print(logo)
print("Welcome to the secret auction program.\n")

while run_again:
    name = input("What's your name?\n")
    bid = int(input("What's your bid?: $"))

    bidders[name] = bid

    option = input('Are there other users who want to bid? Write "Yes" or "No": ').lower()
    if option == "yes":
        clear()
        run_again = True
    else:
        clear()
        biggest_bid(bidders)
        run_again = False