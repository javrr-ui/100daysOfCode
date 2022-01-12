try:
    file = open("a_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["asdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
except KeyError:
    print("That key does not exist")