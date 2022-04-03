import random
import string

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#  'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#   'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#    'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

string_letters = string.ascii_letters
string_numbers = string.digits
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters = []
numbers = []

for n in string_letters:
    letters.append(n)

for n in string_numbers:
    numbers.append(n)

print("Welcome to the PyPassword Generator!")
nb_letters = int(input("How many letters would you like in you password ? "))
nb_symbols = int(input("How many symboles would you like in you password ? "))
nb_numbers = int(input("How many numbers would you like in you password ? "))

password = []

for n in range(0, nb_letters):
    password.append(random.choice(letters))

for n in range(0, nb_numbers):
    password.append(random.choice(numbers))

for n in range(0, nb_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
print(password)
password_final = ""
for char in password:
    password_final += char

print(password_final)
