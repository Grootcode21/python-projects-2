import re

# Stricter regex (allows RFC-like local part atoms, prevents empty domain labels,
# prevents domain labels starting or ending with a hyphen, enforces TLD >= 2 letters)
EMAIL_RE = re.compile(r"""
^
  ([A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+            # local part atom
    (?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*    # dot-separated atoms, no consecutive or edge dots
  )
  @
  (?:                                         # domain: one or more labels followed by TLD
    [A-Za-z0-9]                               # label must start with alphanumeric
    (?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?        # interior chars, hyphens allowed, not at ends
    \.
  )+
  [A-Za-z]{2,}                                # TLD (at least 2 letters)
$
""", re.VERBOSE)

def is_valid_email(email: str) -> bool:
    return EMAIL_RE.fullmatch(email) is not None

if __name__ == "__main__":
    email = input("Enter an email address: ").strip()
    if is_valid_email(email):
        print("The email is valid. ✅")
    else:
        print("❌ Invalid!! ")

