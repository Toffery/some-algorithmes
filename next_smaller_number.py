"""
Description:
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1, when there is no smaller number that contains the same digits.
Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""


def next_smaller(num):
    numbers = list(map(int, str(num)))
    n = len(numbers)
    if n == 1:
        return -1
    for i in range(len(numbers) - 1, 0, -1):
        index = i
        if numbers[i] < numbers[i-1]:
            break
        if i == 1 and numbers[i] >= numbers[i-1]:
            return -1
    num_to_replace = numbers[index-1]
    smallest_index = index
    for j in range(index + 1, n):
        if num_to_replace > numbers[j] > numbers[smallest_index]:
            smallest_index = j
    numbers[index-1], numbers[smallest_index] = numbers[smallest_index], numbers[index-1]
    res = numbers[:index] + sorted(numbers[index:], reverse=True)
    str_res = ''
    for i in res:
        str_res += str(i)
    if str_res.startswith('0'):
        return -1
    return int(str_res)


# Tests
def basicTests():
    assert next_smaller(21) == 12, "Incorrect answer for n=21"
    assert next_smaller(907) == 790, "Incorrect answer for n=907"
    assert next_smaller(531) == 513, "Incorrect answer for n=531"
    assert next_smaller(1027) == -1, "Incorrect answer for n=1027"
    assert next_smaller(441) == 414, "Incorrect answer for n=441"
    assert next_smaller(123456798) == 123456789, "Incorrect answer for n=123456798"


def extendedTests():
    def short():
        assert next_smaller(513) == 351, "Incorrect answer for n=513"
        assert next_smaller(351) == 315, "Incorrect answer for n=351"
        assert next_smaller(315) == 153, "Incorrect answer for n=315"
        assert next_smaller(153) == 135, "Incorrect answer for n=153"
        assert next_smaller(135) == -1, "Incorrect answer for n=135"
        assert next_smaller(100) == -1, "Incorrect answer for n=100"
        assert next_smaller(2071) == 2017, "Incorrect answer for n=2071"
        assert next_smaller(1207) == 1072, "Incorrect answer for n=1207"
        assert next_smaller(414) == 144, "Incorrect answer for n=414"

    def long():
        assert next_smaller(123456789) == -1, "Incorrect answer for n=123456789"
        assert next_smaller(29009) == 20990, "Incorrect answer for n=29009"
        assert next_smaller(1234567908) == 1234567890, "Incorrect answer for n=1234567908"
        assert next_smaller(9999999999) == -1, "Incorrect answer for n=9999999999"
        assert next_smaller(59884848483559) == 59884848459853, "Incorrect answer for n=59884848483559"
        assert next_smaller(1023456789) == -1, "Incorrect answer for n=1023456789"
        assert next_smaller(51226262651257) == 51226262627551, "Incorrect answer for n=51226262651257"
        assert next_smaller(202233445566) == -1, "Incorrect answer for n=202233445566"
        assert next_smaller(506789) == -1, "Incorrect answer for n=506789"

    short()
    long()
    passed = 'All tests passed :)'
    print('-' * len(passed))
    print(passed)
    print('-' * len(passed))


def rndom():
    from random import random
    from math import exp
    from operator import itemgetter

    def refSol(n):
        s = str(n)
        LR_Pairs = list(enumerate(zip(s, s[1:])))
        iP, pivot = next(((i, l) for i, (l, r) in reversed(LR_Pairs) if l > r), (-1, -1))

        if iP == -1: return -1

        iM, m = max(((i, c) for i, c in enumerate(s[iP + 1:], iP + 1) if c < pivot), key=itemgetter(1))
        s = s[:iP] + m + ''.join(sorted(s[iP:iM] + s[iM + 1:], reverse=True))

        return int(s) if s[0] != '0' else -1

    for r in range(500):
        n = round(exp(43 * random()))
        if r % 5:  # Create a huge delta, to disable iterative algorythms
            s = str(n)
            n = n * 10 ** len(s) + int(''.join(sorted(s)))

        expected = refSol(n)
        # print(n-expected)

        assert next_smaller(n) == expected, f"Incorrect answer for n={n}"


extendedTests()
