#Step 3
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"Pssstn the solution is {chosen_word}")

display = []

for n in chosen_word:
    display.append('_')
while display.count('_') >= 1:
    guess = input("Guess a letter: ").lower()
    if chosen_word.count(guess) == 0:
        print(f"{guess} khong dung, vui long nhap vao gia tri khac.")
    elif display.count(guess) == 0:
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                display[n] = guess
        print(display)
    else:
        print(f"{guess} da ton tai.")

print("You win.")