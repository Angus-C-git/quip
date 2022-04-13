import secrets
from quip.constants import (
    DEFAULT_LEN,
    SPECIAL_CHARS,
    DEFAULT_ALPHABET,
    NO_DIGITS_ALPHABET
)


class Generate():
    def __init__(self, length=DEFAULT_LEN, include_special=False, no_digits=False):

        self.length = length if length else DEFAULT_LEN
        self.include_special = include_special
        self.no_digits = no_digits

    def password_candidate(self):
        """
        Generate a password candidate 
        from the given parameters and
        english alphabet.
        """
        alphabet = DEFAULT_ALPHABET
        if self.include_special:
            alphabet += SPECIAL_CHARS
        if self.no_digits:
            alphabet = NO_DIGITS_ALPHABET

        candidate = ''.join(secrets.choice(alphabet)
                            for i in range(self.length))

        if self.include_special:
            if not set(candidate).intersection(set(SPECIAL_CHARS)):
                return self.password_candidate()

        return candidate
