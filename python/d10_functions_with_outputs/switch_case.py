def add(a, b):
    return a + b

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

print('''
    1. Add
    2. Sub
    3. Multiply
    4. Divide
''')

first_nb = int(input("First number? "))
second_nb = int(input("Second number? "))
choice = int(input("What is your choice? "))

operations = [add, subtract, multiply, devide]
output = operations[choice - 1](first_nb, second_nb)
print(output)