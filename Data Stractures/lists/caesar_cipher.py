import string

def encrypt(text, shift):
    alphanumeric_list = list(string.ascii_uppercase)
    cipher_text = ""
    plain_text = text.upper()
    
    for letter in list(plain_text):
        try:
            plain_letter_position = alphanumeric_list.index(letter)
            new_position = (plain_letter_position + shift) % 26
            cipher_letter = alphanumeric_list[new_position]
            cipher_text += cipher_letter
        except ValueError:
            cipher_text += letter
            continue
    return cipher_text

def decrypt(text, shift):
    alphanumeric_list = list(string.ascii_uppercase)
    plain_text = ""
    cipher_text = text.upper()
    
    for letter in list(cipher_text):
        try:
            cipher_letter_position = alphanumeric_list.index(letter)
            new_position = (cipher_letter_position - shift) % 26
            plain_letter = alphanumeric_list[new_position]
            plain_text += plain_letter
        except ValueError:
            plain_text += letter
            continue
    return plain_text


# encrypted_msg = encrypt("Do not stop in your storm!", 4)
# print(f"The encoded message is \"{encrypted_msg}\"") 

encrypted_msg = encrypt("Eric, Hi!", 2)
print(f"The encoded message is \"{encrypted_msg}\"") 

decrypted_msg = decrypt(encrypted_msg, 2)
print(f"The decoded message is \"{decrypted_msg}\"") 
