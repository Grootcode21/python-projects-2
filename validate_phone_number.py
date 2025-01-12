import phonenumbers as pn 
#pip install phonenumbers

def phone_validation(phone_number):
    try:
        parsed_number = pn.parse(phone_number)
        if pn.is_valid_number(parsed_number):
            return pn.format_number(parsed_number, pn.PhoneNumberFormat.E164)

    except pn.NumberParseException:
        return "Invalid phone number"