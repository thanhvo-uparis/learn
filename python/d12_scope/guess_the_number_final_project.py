import random
from art import logo

print(logo)

def random_nb():
    number = random.randint(1, 101)
    return number

def game():
    is_end_game = False
    nb = random_nb()

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {nb}")
    difficul = input("Choose a difficulty. Type 'easy' or 'hard'? ")

    if difficul == "easy":
        attempts = 10
        print("You have 10 attempts remaining to guess the number.")
    else:
        attempts = 5
        print("You have 5 attempts remaining to guess the number.")

    while not is_end_game:
        guess = int(input("Make a guess: "))
        if guess > nb:
            attempts -= 1
            print("To high. \nGuess again.")
        elif guess == nb:
            print(f"You got it! The answer was {guess}.")
            is_end_game = True
            return
        else:
            attempts -= 1
            print("Too low. \nGuess again.")
        
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif attempts == 0:
            print("You lose.")
            is_end_game = True
    
    return attempts

def guess():
    game()

guess()