from password_validator import validate_password

# valid password examples:
assert validate_password("ValidPass123!") == True
assert validate_password("12km$$$J") == True

sample_password = "Sample$"
for i in range(8, 21):
    sample_password += "0"
    assert validate_password(sample_password) == True

# password too short
assert validate_password("Sh0Rt1") == False

# password too long
assert validate_password("ThisPassw0rdisWAYYYTOOOOL@ng") == False

# password does not contain a number
assert validate_password("NonumbersHere!") == False

# password does not contain a symbol
assert validate_password("NumsandChars0nly") == False

# password does not contain an uppercase character
assert validate_password("lowerc4$epassword") == False

# password does not contain a lowercase character
assert validate_password("ANGRYP4SSW0RD") == False

print("All tests passed.")

