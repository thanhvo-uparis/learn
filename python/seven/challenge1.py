#Step 3
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
while not end_game:
  guess = input("Guess a letter: ")
  if not display.count(guess) != 0:
    if chosen_word.count(guess) != 0:
      for n in range(len(chosen_word)):
        if chosen_word[n] == guess:
          display[n] = guess
      print(display)
    else:
      print(f"{guess} khong chinh xac")
  else:
    print(f"{guess} da ton tai trong display")
  
  if "_" not in display:
    end_game = True
    print("You win!")

#baboon
# c : c khong trong babbon et c khong trong display
# b: b trong baboon va b khong trong display
# b: b da ton tai trong display