with open("file.txt") as file:
    content = file.read()
    print(content)

with open("file.txt", mode="a") as file:
    file.write("\nNew Text")
