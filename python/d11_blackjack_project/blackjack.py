import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []
is_game_over = False

for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    if 11 is cards and 10 is cards:
        return 0
    if 11 is cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
print(f"Computer's first card: {computer_cards}")

if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0 or calculate_score(user_cards) > 21:
    is_game_over = True
else:
    check = input("Type 'y' to get another card, type 'n' to pass: ")
    if check == 'y':
        user_cards.append(deal_card)
    else:
        is_game_over = True