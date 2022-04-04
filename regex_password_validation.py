"""
Description:
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
-contains a lowercase letter
-contains an uppercase letter
-contains a number
Valid passwords will only be alphanumeric characters.
"""
from re import search
from random import random, randint


regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[a-zA-Z0-9]{6,}$"
# ^              begin word
# (?=.*?[a-z])   at least one lowercase letter
# (?=.*?[A-Z])   at least one uppercase letter
# (?=.*?[0-9])   at least one number
# [a-zA-Z0-9]     only alphanumeric
# {6,}           at least 6 characters long
# $              end word

assert bool(search(regex, 'fjd3IR9')) is True
assert bool(search(regex, 'ghdfj32')) is False
assert bool(search(regex, 'DSJKHD23')) is False
assert bool(search(regex, 'dsF43')) is False
assert bool(search(regex, '4fdg5Fj3')) is True
assert bool(search(regex, 'DHSJdhjsU')) is False
assert bool(search(regex, 'fjd3IR9.;')) is False
assert bool(search(regex, 'fjd3  IR9')) is False
assert bool(search(regex, 'djI38D55')) is True
assert bool(search(regex, 'a2.d412')) is False
assert bool(search(regex, 'JHD5FJ53')) is False
assert bool(search(regex, '!fdjn345')) is False
assert bool(search(regex, 'jfkdfj3j')) is False
assert bool(search(regex, '123')) is False
assert bool(search(regex, 'abc')) is False
assert bool(search(regex, '123abcABC')) is True
assert bool(search(regex, 'ABC123abc')) is True
assert bool(search(regex, 'Password123')) is True


sol = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
all = "".join([lower, upper, digits])
wrong = " !_+-?/\\"

for _ in range(100):
    s = "".join(sorted([upper[randint(0,len(upper)-1)], lower[randint(0,len(lower)-1)], digits[randint(0,len(digits)-1)]]+[all[randint(0,len(all)-1)] if randint(0,10) else wrong[randint(0,len(wrong)-1)] for q in range(randint(0,15))], key=lambda a: random()))
    assert (search(regex, s) is not None) is (search(sol, s) is not None)

passed = 'All tests passed :)'
print('-' * len(passed))
print(passed)
print('-' * len(passed))
