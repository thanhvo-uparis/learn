import random

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    times = 2
    my_cards = []
    for n in range(times):
        my_cards.append(random.choice(cards))

    current_score = sum(my_cards)
    computer_cards = []
    for n in range(times):
        computer_cards.append(random.choice(cards))

    computer_score = sum(computer_cards)

    print(f"Your cards {my_cards}, current score: {current_score}")
    print(f"Computer's first card: {computer_cards[0]}")

blackjack()

