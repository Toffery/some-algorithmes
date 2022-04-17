"""
(3 kyu) Rail Fence Cipher: Encoding and Decoding
Create two functions to encode and then decode a string using the Rail Fence Cipher.
This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails".
First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally
and up until you reach the top rail. Continue until you reach the end of the string.
Each "rail" is then read left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C
    A       I       V       D       E       N

The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN

Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails,
and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string
will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity.
There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.
"""


def encode_rail_fence_cipher(text, key):
    if text == '':
        return text
    list_rails = [[] for _ in range(key)]
    sep_num = (key - 1) * 2
    sep_text = []
    for i in range(1, len(text) + 1, sep_num):
        sep_text.append(text[i - 1:sep_num + i - 1])
    for txt in sep_text:
        while len(txt) != sep_num:
            txt += '~'
        for i in range(key):
            list_rails[i].append(txt[i])
        for i in range(key - sep_num, 0):
            list_rails[-i].append(txt[i])
    res = ''
    for txt in list_rails:
        for sym in txt:
            res += sym
    res = res.replace('~', '')
    return res


def decode_rail_fence_cipher(cipher, key):
    """
    Build something like this:
    *---*---*
    -*-*-*-*-
    --*---*--
    """
    rails = [['\n' for i in range(len(cipher))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rails[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rails[i][j] == '*') and (index < len(cipher)):
                rails[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rails[row][col] != '*':
            result.append(rails[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


# Tests
def encode_test():
    assert encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) == "WECRLTEERDSOEEFEAOCAIVDEN"
    assert encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 4) == "WIREEEDSEEEACAECVDLTNROFO"
    assert encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 5) == "WCLEESOFECAIVDENRDEEAOERT"
    assert encode_rail_fence_cipher("Hello, World!", 2) == "Hlo ol!el,Wrd"
    assert encode_rail_fence_cipher("Hello, World!", 3) == "Hoo!el,Wrdl l"
    assert encode_rail_fence_cipher("Hello, World!", 4) == "H !e,Wdloollr"
    assert encode_rail_fence_cipher("", 3) == ""

def decode_test():
    assert decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) == "WEAREDISCOVEREDFLEEATONCE"
    assert decode_rail_fence_cipher("WIREEEDSEEEACAECVDLTNROFO", 4) == "WEAREDISCOVEREDFLEEATONCE"
    assert decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 5) == "WLSADOOTEEECEAEECRFINVEDR"
    assert decode_rail_fence_cipher("H !e,Wdloollr", 4) == "Hello, World!"
    assert decode_rail_fence_cipher("", 3) == ""


# Random Tests

from random import randint, choices
from string import ascii_lowercase


def reference_encode(string, n):
    message = ''
    rails = get_rails_sol(string, n)
    for rail in rails:
        message += ''.join(rail)
    return message


def reference_decode(string, n):
    indices = get_indices_sol(string, n)
    rails = get_rails_sol(string, n)
    chars = list(string)
    decoded = []
    for rail in rails:
        temp = chars[0:len(rail)]
        chars = chars[len(rail):len(chars)]
        decoded.append(temp)
    message = ''
    for idx in indices:
        letter = decoded[idx][0]
        decoded[idx] = ''.join(decoded[idx][1:len(decoded[idx])])
        message += letter
    return message


def get_rails_sol(string, n):
    rails = []
    for i in range(0, n):
        rails.append([])
    indices = get_indices_sol(string, n)
    for index, value in enumerate(indices):
        rails[value].append(string[index])
    return rails


def get_indices_sol(string, n):
    seq = list(range(0, n)) + list(range(n - 2, 0, -1))
    indices = [None] * len(string)
    for i in range(0, len(indices)):
        indices[i] = seq[i % len(seq)]
    return indices


def random_encode():
    for _ in range(100):
        s = "".join(choices(ascii_lowercase, k=randint(10, 50)))
        n = randint(2, 10)
        assert encode_rail_fence_cipher(s, n) == reference_encode(s, n)


def random_decode():
    for _ in range(100):
        s = "".join(choices(ascii_lowercase, k=randint(10, 50)))
        n = randint(2, 10)
        assert decode_rail_fence_cipher(s, n) == reference_decode(s, n)


random_encode()
random_decode()
passed = 'All tests passed :)'
print('-' * len(passed))
print(passed)
print('-' * len(passed))
