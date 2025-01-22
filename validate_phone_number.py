import phonenumbers as pn 
#pip install phonenumbers


def phone_validation(phone_number):
    try:
        parsed_number = pn.parse(phone_number)
        if pn.is_valid_number(parsed_number):
            return f"Valid: {pn.format_number(parsed_number, pn.PhoneNumberFormat.E164)}
        else:
        return "Invalid phone number"
    except pn.NumberParseException:
        return "Invalid phone number"

print(phone_validation(700407601))