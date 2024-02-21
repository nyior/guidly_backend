import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6


def _random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))


def generate_slug(word):

    alphanumeric = ""
    word = word.lower()

    for character in word:

        if character == " ":
            alphanumeric += "-"

        if character == "-":
            pass

        if character.isalnum():
            alphanumeric += character

    return alphanumeric + _random_string()
