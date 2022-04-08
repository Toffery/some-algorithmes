"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = lower_letters.upper()
    encoded_message = ''
    for i in message:
        if i.isupper():
            up_index = upper_letters.index(i)
            encoded_message += upper_letters[(up_index+13)%26]
        elif i.islower():
            low_index = lower_letters.index(i)
            encoded_message += lower_letters[(low_index+13)%26]
        else:
            encoded_message += i
    return encoded_message


# Tests
import string
from codecs import encode
import random

sol = lambda s: encode(s, 'rot13')


def static(d):
    assert rot13(d) == sol(d)
    assert rot13(rot13(d)) == d


for _ in range(100):
    word = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + " " + string.digits) for _ in range(16))
    static(word)

passed = 'All tests passed :)'
print('-' * len(passed))
print(passed)
print('-' * len(passed))
