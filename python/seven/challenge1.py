#Step 2
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
guess =input("Guess a letter: ").lower()
print(f"Pssstn the solution is {chosen_word}")

display = []

for n in chosen_word:
    display.append('_')

for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        display[position] = guess
        
print(display)