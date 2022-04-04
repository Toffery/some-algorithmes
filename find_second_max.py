"""
You need to find the second maximum of array.
If array is empty, return None.
If array only have one element, return None.
If array consists of the same values, return None.
"""


def find_second_max(nums):
    if len(nums) <= 1:
        return None
    first_max = float('-inf')
    second_max = float('-inf')
    for i in nums:
        if i == first_max:
            continue
        elif i > first_max:
            second_max = first_max
            first_max = i
        elif i > second_max:
            second_max = i
    return second_max if second_max > float('-inf') else None


def check():
    res = find_second_max([1, 2, 5, 6, 21, 100])
    assert res == 21, f'Wrong answer: {res}'
    res = find_second_max([])
    assert res is None, f'Wrong answer: {res}'
    res = find_second_max([100])
    assert res is None, f'Wrong answer: {res}'
    res = find_second_max([100, 100])
    assert res is None, f'Wrong answer: {res}'
    res = find_second_max([100, 100, 99])
    assert res == 99, f'Wrong answer: {res}'
    res = find_second_max([99, 100])
    assert res == 99, f'Wrong answer: {res}'
    res = find_second_max([10, 100, -100, 20])
    assert res == 20, f'Wrong answer: {res}'
    res = find_second_max([100, 100, 100, 100, 100, 100])
    assert res is None, f'Wrong answer: {res}'
    passed = 'All tests passed :)'
    print('-' * len(passed))
    print(passed)
    print('-' * len(passed))


if __name__ == '__main__':
    check()