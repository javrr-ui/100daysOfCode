#calculator
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for operation in operations:
        print(operation)

    continue_program = True
    while continue_program:

        symbol = input("Pick and operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {symbol} {num2} = {result}")

        choice = input(f'Type "y" to continue caltulating with {result} or type "n" to start a new calculation: ').lower()
        if not choice == "y":
            continue_program = False
            calculator()

        #asign the last result to the variable num1
        num1 = result

calculator()