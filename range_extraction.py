"""
Description:
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints.
It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order
and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org
"""


def solution(numbers):
    valid_list = []
    iterator = iter(range(len(numbers)-1))
    for i in iterator:
        tmp = []
        while numbers[i+1] - numbers[i] == 1:
            tmp.append(numbers[i])
            tmp.append(numbers[i+1])
            try:
                i = next(iterator)
            except:
                break
        if len(tmp) > 2:
            valid_list.append(f'{tmp[0]}-{tmp[-1]}')
        elif len(tmp) == 2:
            valid_list.append(str(tmp[0]))
            valid_list.append(str(tmp[1]))
        if numbers[i] not in tmp:
            valid_list.append(str(numbers[i]))

    if numbers[-1] - numbers[-2] != 1:
        valid_list.append(str(numbers[-1]))
    return ','.join(valid_list)


# Tests
assert solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8,
                 9, 10, 11, 14, 15, 17, 18, 19, 20]) == '-6,-3-1,3-5,7-11,14,15,17-20'
assert solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) == '-3--1,2,10,15,16,18-20'
assert solution([1, 2, 3, 4, 5]) == '1-5'


def solver(args):
    rnge, ans = [], []
    for n1, n2 in zip(args, args[1:] + ['']):
        if n1 + 1 == n2:
            if not rnge:
                rnge = [n1, n2]
            else:
                rnge[1] = n2

        else:
            if rnge:
                if rnge[0] + 1 == rnge[1]:
                    ans.extend(map(str, rnge))
                else:
                    ans.append('-'.join(map(str, rnge)))
                rnge = []
            else:
                ans.append(str(n1))

    return ",".join(ans)


from random import randint

for _ in range(20):
    y = randint(-100, -50)
    x = [y]
    for __ in range(randint(10, 30)):
        y += randint(1, 3)
        x.append(y)
    assert solution(list(x)) == solver(x), "It should work for random inputs too"

passed = 'All tests passed :)'
print('-' * len(passed))
print(passed)
print('-' * len(passed))
