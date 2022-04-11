"""
Create a function that takes a positive integer and returns the next bigger number
that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
"""
from random import randint


def next_bigger(num):
    numbers = list(map(int, str(num)))
    n = len(numbers)
    if n == 1:
        return -1
    for i in range(len(numbers) - 1, 0, -1):
        index = i
        if numbers[i] > numbers[i - 1]:
            break
        if i == 1 and numbers[i] <= numbers[i - 1]:
            return -1
    num_to_replace = numbers[index - 1]
    smallest_index = index
    for j in range(index + 1, n):
        if num_to_replace < numbers[j] < numbers[smallest_index]:
            smallest_index = j

    numbers[index - 1], numbers[smallest_index] = numbers[smallest_index], numbers[index - 1]
    res = numbers[:index] + sorted(numbers[index:])
    str_res = ''
    for i in res:
        str_res += str(i)
    return int(str_res)


# Tests
assert next_bigger(12) == 21
assert next_bigger(513) == 531
assert next_bigger(2017) == 2071
assert next_bigger(414) == 441
assert next_bigger(144) == 414

assert next_bigger(123456789) == 123456798
assert next_bigger(1234567890) == 1234567908
assert next_bigger(9876543210) == -1
assert next_bigger(9999999999) == -1
assert next_bigger(59884848459853) == 59884848483559


def next_sol(n):
    n, temp = list(str(n)), []
    i = len(n) - 1
    while i > 0 and n[i - 1] >= n[i]:
        temp += [n[i]]
        i -= 1
    temp += [n[i]]
    i -= 1
    if i == -1: return i
    top = n[i]
    j = int(top) + 1
    while str(j) not in temp: j += 1
    temp.remove(str(j))
    temp += [top]
    temp.sort()
    temp = [str(j)] + temp
    return int("".join(n[:i] + temp))


for _ in range(140):
    n = randint(1, 10 ** randint(1, 14))
    if randint(1, 100) < 10: n = int("".join(sorted(str(n), reverse=True)))
    assert next_bigger(n) == next_sol(n), "It should work for random inputs too"

passed = 'All tests passed :)'
print('-' * len(passed))
print(passed)
print('-' * len(passed))
