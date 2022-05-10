import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(f"user cards: {user_cards}")
print(f"computer cards: {computer_cards}")

def calculate_score(cards):
    if cards == [11, 10] or cards == [10, 11]:
        return 0
    if 11 is cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# def blackjack():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
#     my_cards = []
#     computer_cards = []
#     times = 2
#     for n in range(times):
#         my_cards.append(random.choice(cards))
#         computer_cards.append(random.choice(cards))
#     current_score = sum(my_cards)
#     computer_score = sum(computer_cards)
#     verifier = True
#     while verifier:
#         print(f"Your cards {my_cards}, current score: {current_score}")
#         print(f"Computer's first card: {computer_cards[0]}")
#         choice = input("Type 'y' to get another card, type 'n' to pass: ")
#         if current_score > 21:
#             verifier = False
#             print("Your lose!")
#         elif choice == 'y':
#             my_cards.append(random.choice(cards))
#             computer_cards.append(random.choice(cards))
#             blackjack()
#         else:
#             if current_score > computer_score:
#                 print("You win!")
#                 verifier = False
#             elif current_score < computer_score:
#                 print("You lose!")
#                 verifier = False
#             else: 
#                 print("Hoa nhau!")
#                 verifier = False

# blackjack()

