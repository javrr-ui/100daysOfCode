
with open("file1.txt") as file1:
    list_1 = file1.readlines()
    list_1 = [int(number.strip()) for number in list_1]

# Write your code above 👆

print(result)
