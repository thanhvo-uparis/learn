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
    if direction=="encode":
        for n in plain_text:
            index_of_letter = alphabet.index(n)
            cipher_text += alphabet[index_of_letter + shift]
        print(f"The encoded text is {cipher_text}")
    else:
        for n in plain_text:
            index_of_letter = alphabet.index(n)
            cipher_text += alphabet[index_of_letter - shift]
        print(cipher_text)

encrypt(plain_text=text, shift=shift)