import random
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

random_nb = random.randint(1, len(names) -1)
print(f"{names[random_nb]} is going to buy the meal today!")