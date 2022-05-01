# def my_func(a,b):
#     if a + b < 10:
#         print("")
#         return
#     return a + b

# print(my_func(5,4))

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
    "/": devide,
}

num1 = int(input("First number? "))
for key in operations:
    print(key)
choice = input("What is operation: ")
num2 = int(input("Second number? "))
output = operations.get(choice)(num1, num2)
print(f"{num1} {choice} {num2} = {output}.")