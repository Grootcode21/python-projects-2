password = input("Please enter your password: ")

def validate_password():
    if len(password) < 8:
        print("Your password is too short")
    elif not any(char.isupper() for char in password):
         print("Your password does not have an upper case")
    elif not any(char.islower() for char in password):
        print("Your password does not have a lower case")
    elif not any(char.isdigit() for char in password):
        print("Your password does not have a digit")
    elif not any(char in "!@#$%^&*" for char in password):
        print("Your password does not have special character-s")
    elif " " in password:
        print("Your password contains spaces")
    else:
        print("Your password is password")

validate_password()