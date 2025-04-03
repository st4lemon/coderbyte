"""
Length: Must be between 8 and 20 characters inclusive
Character types: must have
- 1 uppercase
- 1 lowercase
- 1 numeric digit
- 1 special digit from !@#$%^&*()
"""
def validate_password(password: str) -> bool:
    chars = "!@#$%^&*()"
    upper = False
    lower = False
    numer = False
    spec = False
    if not 8 <= len(password) <= 20:
        return False
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isnumeric():
            numer = True
        elif chars.find(ch) >= 0:
            spec = True
    return upper and lower and numer and spec

        
