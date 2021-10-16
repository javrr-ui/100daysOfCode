import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userInput = input("What do you choose? Type 0 for Rock, 1 for Paper and  2 for Scissors.\n")
userInput = int(userInput)
computer = random.randint(0,2)

if userInput == 0:
    print(rock)
elif userInput ==1:
    print(paper)
else:
    print(scissors)

print("Computer choose:")

if computer == 0:
    print(rock)
elif computer ==1:
    print(paper)
else:
    print(scissors)

if (userInput == 2 and computer == 1) or (userInput == 1 and computer == 0) or (userInput == 0 and computer == 2):
    print("You win")
elif userInput == computer:
    print("Draw")
else:
    print("You lose")