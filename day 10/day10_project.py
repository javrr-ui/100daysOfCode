#calculator


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

num1 = int(input("What's the first number?: "))

for operation in operations:
    print(operation)

symbol = input("Pick and operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculation_function = operations[symbol]
result = calculation_function(num1, num2)

print(f"{num1} {operation} {num2} = {result}")