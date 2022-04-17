import string

# letters = string.ascii_lowercase
# # alphabet = []
# # for n in letters:
# #     alphabet.append(n)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#hello
#5
#
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(plain_text, shift):
    cipher_text = ""
    for n in plain_text:
        index_of_letter = alphabet.index(n)
        cipher_text += alphabet[index_of_letter + shift]
    print(f"The encoded text is {cipher_text}")
        
def decrypt(plain_text, shift):
    cipher_text = ""
    for n in plain_text:
        index_of_letter = alphabet.index(n)
        cipher_text += alphabet[index_of_letter - shift]
    print(f"The decoded text is {cipher_text}")

if direction == "encode":
    encrypt(plain_text=text, shift=shift)
else:
    decrypt(plain_text=text, shift=shift)