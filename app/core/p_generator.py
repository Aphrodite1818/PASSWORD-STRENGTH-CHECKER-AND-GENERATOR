##--------------------------------THIS SCRIPT IS FOR GENERATING A PASSWORD--------------------------------##
import string
import random
from pathlib import Path
import sys



"""
    Generates a random password using configuration from config.py
    the password length, whether to include numbers, and whether to include special characters,
    can be modified in Utils/config.py dir
"""

def gen_password(NUMBERS,SPECIAL_CHARACTERS,LENGTH,SHUFFLE):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password_chars = []


    first_char = random.choice(lowercase_letters + uppercase_letters)
    password_chars.append(first_char)


    if first_char.islower():
        password_chars.append(random.choice(uppercase_letters))


    elif first_char.isupper():
        password_chars.append(random.choice(lowercase_letters))


    #else:
        #password_chars.append(random.choice(lowercase_letters + uppercase_letters))  # fallback

    if NUMBERS:
        password_chars.append(random.choice(digits))

    
    if SPECIAL_CHARACTERS:
        password_chars.append(random.choice(special))

    

    ## Fill the rest of the password length with random choices from the allowed characters ##
    all_characters = lowercase_letters + uppercase_letters
    if NUMBERS:
        all_characters += digits
    if SPECIAL_CHARACTERS:
        all_characters += special

    
    while len(password_chars) < LENGTH:
        password_chars.append(random.choice(all_characters))

    if SHUFFLE:
        rest_chars = password_chars[1:]
        random.shuffle(rest_chars)
        password_chars[1:] = rest_chars

    gen_password = ''.join(password_chars)
    return gen_password


if __name__ == "__main__":
    print("Generated Password:", gen_password())