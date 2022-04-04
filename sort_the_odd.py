"""
You will be given an array of numbers.
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples:
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def sort_array(source_array):
    even_numbers = []
    even_indexes = []
    odd_numbers = []
    odd_indexes = []
    for i, num in enumerate(source_array):
        if num % 2 == 0:
            even_numbers.append(num)
            even_indexes.append(source_array.index(num, i))
        else:
            odd_numbers.append(num)
            odd_indexes.append(source_array.index(num))
    tmp_array = sorted(odd_numbers)
    for num, index in zip(even_numbers, even_indexes):
        tmp_array.insert(index, num)
    return tmp_array


"""
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
"""
