import string

# letters = string.ascii_lowercase
# # alphabet = []
# # for n in letters:
# #     alphabet.append(n)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def caesar(plain_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction != "encode":
        shift_amount *= -1
    for n in plain_text:
        index_letter = alphabet.index(n)
        end_text += alphabet[index_letter + shift_amount]
    print(f"Here's the {cipher_direction}, result: {end_text}")  

caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)