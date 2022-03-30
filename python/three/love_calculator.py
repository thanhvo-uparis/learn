print("Welcome to the Love Calculator!")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
name_string = name1.lower() + name2.lower()

true_value = name_string.count("t") + name_string.count("r") + name_string.count("u") + name_string.count("e")
love_value = name_string.count("l") + name_string.count("o") + name_string.count("v") + name_string.count("e")
score = int(str(true_value) + str(love_value))

myString = ""
if score <10 or score > 90:
    myString += ", you go together like coke and mentos"
elif score >= 40 and score <= 50:
    myString += ", you are alright together"
else:
    myString = ""

print(f"Your score is {score}{myString}.")