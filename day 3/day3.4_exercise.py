# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "l" or size == "L":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
    bill += 25
elif size == "m" or size == "M":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 3
    bill += 20
elif size == "s" or size == "S":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        bill += 2
    bill += 15
else:
    bill += 15
if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}.")