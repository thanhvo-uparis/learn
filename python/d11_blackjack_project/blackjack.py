import random

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    user_card = []
    computer_card = []

    for n in range(2):
        user_card.append(random.choice(cards))
        computer_card.append(random.choice(cards))
    return user_card, computer_card

def calculate_score(l1, l2):
    if l1 == [10, 11] or l1 == [11,10]:
        print("You win")
    elif l2 == [10, 11] or l2 == [11, 10]:
        print("Computer lose")
    return sum(l1), sum(l2)

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

