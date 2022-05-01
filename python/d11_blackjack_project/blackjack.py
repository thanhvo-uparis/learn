import random

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    times = 2
    my_deck = []
    for n in range(times):
        my_deck.append(random.choice(cards))

    my_total = sum(my_deck)
    computer_deck = []
    for n in range(times):
        computer_deck.append(random.choice(cards))

    computer_total_score = sum(computer_deck)

    print(f"Your cards {my_deck}, current score: {my_total}")
    print(f"Computer's first card: {computer_deck[0]}")

blackjack()

