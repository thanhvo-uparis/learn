import random

word_list = ["ardvark", "baboon", "camel"]
list = random.choice(word_list)
print(list)

mot = input("Guess a letter: ")
for n in range(0, len(list)):
    if list[n] == mot:
        print("Right")
    else:
        print("Wrong")
