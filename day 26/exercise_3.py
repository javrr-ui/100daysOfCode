
with open("file1.txt") as file1:
    list_1 = file1.readlines()
    list_1 = [int(number.strip()) for number in list_1]

with open("file2.txt") as file2:
    list_1 = file2.readlines()
    list_1 = [int(number.strip()) for number in list_2]

# Write your code above 👆

print(result)
