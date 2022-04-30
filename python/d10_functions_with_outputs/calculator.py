from unicodedata import numeric


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

num1 = int(input("What's the first number? "))
for key in operations: 
    print(key)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number? "))
output1 = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} is {output1}")
num3 = int(input("What's the number 3? "))
operation_symbol = input("Pick an operation from the line above: ")
output2 = operations[operation_symbol](output1, num3)
print(f"{output1} {operation_symbol} {num3} is {output2}")

# choice = input("Choice: ")
# output = dictionary.get(choice)(first_nb, second_nb)
# print(output)