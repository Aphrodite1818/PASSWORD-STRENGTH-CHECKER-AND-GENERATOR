##--------------------------------THIS SCRIPT IS FOR CHECKING THE STRENGTH OF THE PASSWORD--------------------------------##

import math
import string


"""
    This function calculates the entropy of a password based on the character pool size.
    It takes a password as input and returns the entropy in bits.
"""

def calculate_entropy(password):
    pool_size = 0 
    length_pd = len(password)

    if any(p.isupper() for p in password):
       pool_size += 26  



    if any(p.islower() for p in password):
        pool_size += 26



    if any(p.isdigit() for p in password):
         pool_size += 10

    if any(p in string.punctuation for p in password):
        pool_size += len(string.punctuation)


    try:
        if pool_size >0:
            bits = length_pd * math.log2(pool_size)
            return bits
    except:
        raise ValueError("Password must contain at least one character from a valid set.")
    

if __name__ == "__main__":
    Password = input("Enter your password: ")
    entropy_test=calculate_entropy(Password)  # Example usage
    print(entropy_test)