from email_validator import EmailValidator, EmailNotValidError

#pip install email_validator

def is_valid_email(email):
    try:
        valid = validate_email(email)
        return f"valid: (valid.email)"