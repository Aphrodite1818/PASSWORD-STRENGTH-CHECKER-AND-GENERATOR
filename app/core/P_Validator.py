##--------------------------------THIS SCRIPT IS FOR CHECKING AND VALIDATING PASSWORD FORMAT--------------------------------##
import string

"""
    This function helps to validate a password based on certain criteria
    defined below. It checks for length, presence of lowercase letters,
    uppercase letters, digits, and special characters.
    you can modify the criteria as needed.
"""

def Password_Validator(Password):
    feedback = []   #--> empty list to store feedback messages

    if len(Password) < 8:
        feedback.append("Password must be at least 8 characters long.")
    

    if not any(p.islower() for p in Password):
        feedback.append("Password must contain at least one lowercase letter.")
    
    if not any(p.isupper() for p in Password):
        feedback.append("Password must contain at least one uppercase letter.")
    
    if not any(p.isdigit() for p in Password):
        feedback.append("Password must contain at least one digit.")
    
    if not any(p in string.punctuation for p in Password):
        feedback.append("Password must contain at least one special character.")

    if feedback:
        return " ".join(feedback)
    

    else:
        return "Password meets all requirements."
    


if __name__ == "__main__":
    Password = input("Enter your password: ")
    result = Password_Validator(Password)
    print(result)