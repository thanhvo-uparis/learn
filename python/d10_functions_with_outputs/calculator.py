import os

def add(a, b):
    return a + b

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}

def calculator():
    num1 = int(input("What's the first number? "))
    for key in operations:
        print(key)

    verifier = True
    while verifier:
        operation_symbol = input("Pick an operation: ")
        next_nb = int(input("What's the next number? ")) 
        output = operations[operation_symbol](num1, next_nb)
        print(f"{num1} {operation_symbol} {next_nb} = {output}.")
        continue_calcul = input(f"Type 'y' to continue calculating with {output}, or type 'n' to exit. ")
        if continue_calcul=='y':
            num1 = output
        else:
            verifier = False
            os.system("clear")

calculator()