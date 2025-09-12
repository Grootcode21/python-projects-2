import re

def is_valid_password(password: str) -> bool:
    # At least 8 characters
    if len(password) < 8:
        return False
    # At least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    # At least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    # At least one digit
    if not re.search(r"\d", password):
        return False
    # At least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

if __name__ == "__main__":
    password = input("Enter a password: ").strip()
    if is_valid_password(password):
        print("✅ The password is strong and valid.")
    else:
        print("❌ The password does not meet security requirements.")
