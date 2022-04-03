# 0: rock (bua)
# 1 paper 
# 2 scissors (keo)
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
choice_pc = random.randint(0,2)

print(choice_pc)

if choice == 0:
    print(rock)
elif choice_pc == 1:
    print(f"Computer chose:\n {paper}\nYou lose")
elif choice_pc == 2:
    print(f"Computer chose:\n {scissors}\nYou win")
else:
    print(f"Computer chose:\n {rock}\nBan hoa")

# program not run
# if choice == 0: 
#     print(rock)
#     if choice_pc == 1:
#         print(f"Computer chose:\n {paper}\nYou lose")
#     elif choice_pc == 2:
#         print(f"Computer chose:\n {scissors}\nYou win")
#     else:
#         print(f"Computer chose:\n {rock}\nBan hoa")
# else:
#     print("ket thuc game")



