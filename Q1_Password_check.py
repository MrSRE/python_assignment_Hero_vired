import re
def check_password_strength(password):
    """Check the strength of a password.
    Args:
    password (str): The password to check.
    Returns:
    bool: True if the password meets the criteria, False otherwise.
    """
    if len(password) < 8:
        return False    
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True
def main():
    password = input("Enter a password to check its strength: ")
    if check_password_strength(password):
        print("The password is strong.")
    else:
        print("The password is weak. Ensure it is at least 8 characters long, contains both uppercase and lowercase letters, at least one digit, and at least one special character.")

if __name__ == "__main__":
    main()
