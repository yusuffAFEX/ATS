import string
from this import s


def determine(word: str):
    if word.isupper():
        return "It is uppercase"
    elif word.islower():
        return "It is lowercase"
    else:
        return "It is both"

print(determine('book'))