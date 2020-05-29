# Complete the method which accepts an array of integers, and returns one of the following:

# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise
# You can assume the array will always be valid, and there will always be one correct answer.

def is_sorted_and_how(arr):
    if max(arr) == arr[-1] and min(arr) == arr[0]:
        return 'yes, ascending'
    elif min(arr) == arr[-1] and max(arr) == arr[0]:
        return 'yes, descending'
    else:
        return 'no'

print(is_sorted_and_how([1, 2]))

print(is_sorted_and_how([15, 7, 3, -8]))

print(is_sorted_and_how([4, 2, 30]))

print('#' * 99)

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr, reverse=True):
        return 'yes, descending'
    else:
        return 'no'

print(is_sorted_and_how([1, 2]))

print(is_sorted_and_how([15, 7, 3, -8]))

print(is_sorted_and_how([4, 2, 30]))

print('#' * 99)
# using ternary operator in Python - Ternary operators are more commonly known as conditional expressions in Python. These operators evaluate something based on a condition being true or not.
# Syntax : [on_true] if [expression] else [on_false] if [expression] else [on_false]
def is_sorted_and_how(arr):
    s = sorted(arr)
    return 'yes, ascending' if arr==s else 'yes, descending' if arr == s[::-1] else 'no'

print(is_sorted_and_how([1, 2]))

print(is_sorted_and_how([15, 7, 3, -8]))

print(is_sorted_and_how([4, 2, 30]))