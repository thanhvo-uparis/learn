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

def find_winner(dic):
    max_bids = 0
    name_key = ""
    for key in dic:
        if dic[key] > max_bids:
            max_bids = dic[key]
            name_key = key
    
    print(f"The winner is {name_key} with a bid of ${max_bids}")

while not response:
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))
    res = input("Are there any other bidders? 'yes' or 'no'. ")

    add_user(name_user=name, bid_value=bid)
    if res=='no':
        response = True
        find_winner(bids)