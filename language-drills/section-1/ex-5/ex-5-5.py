class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

try:
    validate_age(-5)
except InvalidAgeError as e:
    print(e)
