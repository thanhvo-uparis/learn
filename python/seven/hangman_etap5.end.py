#Step 5
import random

from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
display  = []
for n in chosen_word:
    display.append("_")

end_of_game = False
lives = 6

print(logo)
print(f"Pssst, the solution is {chosen_word}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for n in range(len(chosen_word)):
        if chosen_word[n] == guess:
            display[n] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(display)

    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win")

# b trong display, 
