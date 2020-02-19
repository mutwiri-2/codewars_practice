# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


def sort_array(source_array):
    for index1, num1 in enumerate(source_array):
        if num1 % 2 == 1:
            for index2, num2 in enumerate(source_array):
                if num2 % 2 == 1 and num2 != num1:
                    if num2 < num1:
                        source_array[index1] = num2
                        source_array[index2] = num1
        return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))

