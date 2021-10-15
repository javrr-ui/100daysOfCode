print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
decision = input('You\'re at a maze, there\'s two ways, where shall you go, "left" or "right"?\n').lower()

if decision == "l" or decision == "left":
    decision = input(
        'You found a way out of the maze, now you\'re at the beach, there\'s an island a few miles away, will you "swim" or "wait"?\n').lower()
    if decision == "wait" or decision == "w":
        decision = input("While waiting you found a boat hidden in some bushes, you arrived at the island, there\'s a building with 3 doors. One red, one yellow and one blue, which one do you choose?\n").lower()
        if decision == "red" or decision == "r":
            print("The room you entered is suddenly in fire.\nGame over")
        elif decision == "yellow" or decision == "y":
            print("You found the treasure, you win!")
        elif decision == "blue" or decision == "b":
            print("You entered a room full of monsters.\nGame over")
        else:
            print("You\'ve been eaten by big foot.\nGame over")
    else:
        print("You\'ve been atacked by electric eels.\nGame over")
else:
    print("You fell into hole with snakes.\nGame over.")
