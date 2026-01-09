##--------------------------------THIS SCRIPT IS FOR CHECKING THE ENTROPY OF A PASSWORD--------------------------------##
import string
import random
from utils.config import NUMBERS, SPECIAL_CHARACTERS, LENGTH


def gen_password(NUMBERS,SPECIAL_CHARACTERS,LENGTH):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation



    characters = letters
    if NUMBERS:
        characters += digits
    if SPECIAL_CHARACTERS:
        characters += special

    
    password = random.choice(letters)