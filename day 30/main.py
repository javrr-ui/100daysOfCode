try:
    file = open("a_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["asdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)