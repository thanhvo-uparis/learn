#Step 5
import random

word_list = ["aardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
print(f"Pssstn the solution is {chosen_word}")

display = []

for n in range(len(chosen_word)):
    display.append("_")

end_game = False
compter = 6
print(stages[compter])
while not end_game or not compter==0:
  guess = input("Guess a letter: ")
  if not display.count(guess) != 0:
    if chosen_word.count(guess) != 0:
      for n in range(len(chosen_word)):
        if chosen_word[n] == guess:
          display[n] = guess
      print(display)
    else:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      compter -= 1
      print(stages[compter])
  else:
    print(f"You've already guessed {guess}")
  
  if "_" not in display:
    end_game = True
    print("You win!")

#baboon
# c : c khong trong babbon et c khong trong display
# b: b trong baboon va b khong trong display
# b: b da ton tai trong display