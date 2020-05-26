# Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

# #Examples

# maximum([4,6,2,1,9,63,-134,566]) returns 566
# minimum([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximum([5]) returns 5
# minimum([42, 54, 65, 87, 0]) returns 0

# #Notes
# You may consider that there will not be any empty arrays/vectors.

def minimum(arr):
    smallest = arr[0]
    for i in arr[1:]:
        if i<smallest:
            smallest = i
    return smallest

def maximum(arr):
    largest = arr[0]
    for i in arr[1:]:
        if i>largest:
            largest = i
    return largest

print(maximum([4,6,2,1,9,63,-134,566])) # returns 566
print(minimum([-52, 56, 30, 29, -54, 0, -110])) #returns -110
print(maximum([5])) #returns 5
print(minimum([42, 54, 65, 87, 0])) #returns 0

print('#' * 99)

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

print(maximum([4,6,2,1,9,63,-134,566])) # returns 566
print(minimum([-52, 56, 30, 29, -54, 0, -110])) #returns -110
print(maximum([5])) #returns 5
print(minimum([42, 54, 65, 87, 0])) #returns 0

print('#' * 99)

