#Step 3
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"Pssstn the solution is {chosen_word}")

display = []

for n in chosen_word:
    display.append('_')
while display.count('_') >= 1:
    guess =input("Guess a letter: ").lower()
    if display.count(guess) == 0:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
                print(display)
