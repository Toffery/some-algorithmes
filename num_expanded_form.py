"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""

from functools import reduce
from random import randint


def expanded_form(num):
    num = str(num)
    num = num[::-1]
    new_lst = []
    for i in range(len(num)):
        if num[i] != '0':
            new_lst.append(num[i] + '0'*i)
    new_lst = new_lst[::-1]
    res = reduce(lambda x, y: x + ' + ' + y, new_lst)
    return res


def solution(num):
    string = str(num)
    answer = ''
    for i in range(1, len(string)+1):
        num = string[len(string)-i]
        if num == '0':
            pass
        else:
            for j in range(0, i-1):
                num += '0'
            if answer == '':
                answer = num
            else:
                answer = num + ' + ' + answer
    return answer


def tests():
    assert expanded_form(2) == '2'
    assert expanded_form(12) == '10 + 2'
    assert expanded_form(42) == '40 + 2'
    assert expanded_form(70304) == '70000 + 300 + 4'
    assert expanded_form(4982342) == '4000000 + 900000 + 80000 + 2000 + 300 + 40 + 2'

    # Edge cases
    assert expanded_form(420370022) == '400000000 + 20000000 + 300000 + 70000 + 20 + 2'
    assert expanded_form(70304) == '70000 + 300 + 4'
    assert expanded_form(9000000) == '9000000'
    assert expanded_form(92093403034573) == '90000000000000 + 2000000000000 + 90000000000 + 3000000000 + ' \
                                            '400000000 + 3000000 + 30000 + 4000 + 500 + 70 + 3'
    assert expanded_form(2096039485293) == '2000000000000 + 90000000000 + 6000000000 + 30000000 + 9000000 + ' \
                                           '400000 + 80000 + 5000 + 200 + 90 + 3'
    for x in range(0, 100):
        num = randint(1, 1000000)
        res = expanded_form(num)
        assert res == solution(num)
    passed = 'All tests passed :)'
    print('-' * len(passed))
    print(passed)
    print('-' * len(passed))
    return True


if __name__ == '__main__':
    tests()
