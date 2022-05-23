import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'? ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(guess, answer, turns):
    """
    Vérifier si l'entrée de l'utilisateur supérieur ou inférieur ou égale le nombre a généré en aléatoire.
    """
    if guess > answer:
        print("To high. \nGuess again.")
        return turns - 1
    elif guess < answer:
        print("To low. \nGuess again.")
        return turns - 1
    else:
        print("You got it! The answer was {answer}.")

def game():
    # print("Welcome to the Number Guessing Game!")
    # print("I'm thinking of a number between 1 and 100.")
    # answer = random.randint(1, 101)
    # print(f"Pssst, the correct answer is {answer}.")

    # turns = set_difficulty()
    # print(f"You have {turns} attempts remaining to guess the number.")
    # guess = int(input("Make a guess: "))

    # while guess != answer:
    #     turns = check_answer(guess, answer, turns)
    #     if turns == 0:
    #         print("You've run out of guesses, you lose.")
    #         return
    #     elif guess != answer:
    #         print("Guess again.")
game()