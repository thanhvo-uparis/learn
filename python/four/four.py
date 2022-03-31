import random

# random.randint(a,b): random gia tri gia giua a va b
# vd: random_int = random.randint(2, 15)
# print(random_int)

# random.random(): random so thap phan float, gia tri tu 0 - 1.0

# In ra gia tri cua 1 bien trong 1 module khac
# luu y: can import module do 
# vd: print(my_module.today)

number_random = random.randint(0, 5) + random.random()
print(number_random)