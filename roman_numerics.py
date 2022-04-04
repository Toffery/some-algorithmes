"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
It should follow the API demonstrated in the examples below.
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit
and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
"""
from functools import reduce


def expanded_form(num):
    num = str(num)
    num = num[::-1]
    new_lst = []
    for i in range(len(num)):
        if num[i] != '0':
            new_lst.append(num[i] + '0'*i)
    new_lst = new_lst[::-1]
    res = reduce(lambda x, y: x + ' + ' + y, new_lst)
    return new_lst


from_roman_dict = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500,
    'M': 1000
    }

roman_dict = {
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
    40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
    400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }


class RomanNumerals:

    def to_roman(arab_num):
        res = []
        expanded_num = expanded_form(arab_num)
        for i in expanded_num:
            if int(i) in roman_dict.keys():
                res.append(roman_dict[int(i)])
            elif len(i) == 1:
                if int(i) < 4:
                    res.append('I' * int(i))
                elif 5 < int(i) < 9:
                    res.append('V'+('I' * (int(i) % 5)))
            elif len(i) == 2:
                if int(i) < 40:
                    res.append('X' * (int(i) // 10))
                elif 50 < int(i) < 90:
                    res.append('L'+('X' * (int(i) % 50 // 10)))
            elif len(i) == 3:
                if int(i) < 400:
                    res.append('C' * (int(i) // 100))
                elif 500 < int(i) < 900:
                    res.append('D'+ ('C' * (int(i) % 500 // 100)))
            elif len(i) == 4:
                res.append('M' * (int(i) // 1000))
        return ''.join(res)

    def from_roman(roman_num):
        arab_num = 0
        prev_num = from_roman_dict[roman_num[0]]
        arab_num += prev_num
        for i in roman_num[1:]:
            next_num = from_roman_dict[i]
            if next_num <= prev_num:
                arab_num += next_num
                prev_num = next_num
            else:
                arab_num += next_num
                arab_num -= prev_num
                arab_num -= prev_num
                prev_num = next_num
        return arab_num


ROMANS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'C': 100,
    'XC': 90,
    'L': 50,
    'X': 10,
    'V': 5,
    'IV': 4,
    'I': 1,
}


# Good Solution
class GoodRomanNumerals:

    def to_roman(n):
        s = ''
        for key, value in ROMANS.items():
            while n % value != n:
                n = n - value
                s += key
        return s

    def from_roman(r):
        s = 0
        for key, value in ROMANS.items():
            while r.startswith(key):
                r = r[len(key):]
                s += value
        return s