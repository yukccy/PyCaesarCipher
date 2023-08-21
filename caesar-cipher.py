import string
from art import logo

alphabet = list(string.ascii_lowercase)

def caesar(start_text, shift_amount, cipher_direction):
    alphabet_list_len = len(alphabet)
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
        alphabet_list_len *= -1
    for letter in start_text:
        if letter in alphabet:
            list_index = alphabet.index(letter)
            if list_index + shift_amount < abs(alphabet_list_len) and list_index + shift_amount >= 0:
                new_index = list_index + shift_amount
                end_text += alphabet[new_index]
            else:
                new_index = list_index + shift_amount - alphabet_list_len
                end_text += alphabet[new_index]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

print(logo)
should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")