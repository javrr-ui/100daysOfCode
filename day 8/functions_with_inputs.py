# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello")
#     print("Hello")
#     print("Hello")

# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do yo do {name}?")

# greet_with_name("Javier")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Positional Arguments
greet_with("Javier","Los Ángeles")

# Keyword Arguments

greet_with(location="Los Angeles", name="Javier")