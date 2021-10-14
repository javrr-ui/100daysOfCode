# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
firstDigit = 0
secondDigit = 0
string = (name1 + name2).lower()

firstDigit += string.count("t")
firstDigit += string.count("r")
firstDigit += string.count("u")
firstDigit += string.count("e")

secondDigit += string.count("l")
secondDigit += string.count("o")
secondDigit += string.count("v")
secondDigit += string.count("e")

loveScore = int(str(firstDigit) + str(secondDigit))

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore > 40 and loveScore < 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")


