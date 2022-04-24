from art import logo

print(logo)
print("Welcome to the secret auction program.")

response = False
bids = {}
# {
#     "nicola": 20,
#     "vincent": 100
# }
def add_user(name_user, bid_value):
    bids[name_user] = bid_value

max_bids = 0
def find_winner(dic, max_value):
    for key in dic:
        if dic[key] > max_value:
            max_value = dic[key]
    # print(max_value)

while not response:
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))
    res = input("Are there any other bidders? 'yes' or 'no'. ")

    add_user(name_user=name, bid_value=bid)
    find_winner(dic=bids, max_value=max_bids)
    # find_winner(list=bids)
    # print(max_value)
    if res=='no':
        response = True

print(max_bids)
