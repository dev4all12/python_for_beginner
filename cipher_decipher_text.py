# cipher/decipher text
import string

alphabate = list(string.ascii_lowercase)


def enc(plain_text, shift_key):
    cipher_text = ''
    for char in plain_text:
        if char in alphabate:
            position = alphabate.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabate[new_position]
        else:
            cipher_text += char
    print(f"Your cipher text is :{cipher_text}")


def dec(cipher_text, shift_key):
    decipher_text = ''
    for char in cipher_text:
        if char in alphabate:

            position = alphabate.index(char)
            new_position = (position - shift_key) % 26
            decipher_text += alphabate[new_position]
        else:
            decipher_text += char
    print(f"Your decipher text is: {decipher_text}")


wanna_end = False
while not wanna_end:

    what_to_do = input(
        "What you want 'encrypt' or 'decrypt'? Type 'encrypt' or 'decrypt: ")
    text = input("Enter text\n")
    shift = int(input("Entr shift key(0-9)\n"))
    if what_to_do == 'encrypt':

        enc(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        dec(cipher_text=text, shift_key=shift)
    play_again = input("Wanna to play again 'yes' or 'no': ")
    if play_again == 'no':
        wanna_end = True
        print("Thanks Good Bye")
