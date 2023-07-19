#!/usr/bin/python3
def validate_password(password):
    # Check the length of the password
    if len(password) < 8:
        return False
    # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    if not (has_upper and has_lower and has_digit):
        return False
    # Check if the password contains spaces
    if ' ' in password:
        return False
    # If all checks pass, the password is valid
    return True
