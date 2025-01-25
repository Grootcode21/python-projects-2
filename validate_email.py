from email_validator import validate_email, EmailNotValidError

#pip install email_validator

def is_valid_email(email):
    try:
        valid = validate_email(email)
        return f"valid: (valid.email)"

    except EmailNotValidError as e:
        return f"Invalid: {str(e)}"


print(is_valid_email("user@example.com"))
print(is_valid_email("invalid email"))
print(is_valid_email("itmindspace@gmail.com"))