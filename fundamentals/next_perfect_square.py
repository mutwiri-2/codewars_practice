# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

# Examples:

# findNextSquare(121) --> returns 144
# findNextSquare(625) --> returns 676
# findNextSquare(114) --> returns -1 since 114 is not a perfect

def find_next_square(sq):
    i = 0
    while i**2 <= sq:
        if i*i == sq:
            return (i+1)**2
        else:
            i += 1
    return -1

print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))

print('#' * 99)
# second attempt - shorter version

def find_next_square(sq):
    for i in range(sq):
        if i ** 2 == sq:
            return (i+1) ** 2
    return -1

print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))
print(find_next_square(319225))
print(find_next_square(15241383936))

print('#' * 99)

# The above two solutions get timed out -- so Codewars advices one to optimize his / her code

def find_next_square(sq):
    root = sq ** 0.5
    # return (root + 1)**2 if root.is_integer() else -1
    # return -1 if root % 1 else (root + 1)**2
    return (int(root) + 1)**2 if root.is_integer() else -1

print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))
print(find_next_square(319225))
print(find_next_square(15241383936))

print('#' * 99)
# use the math module
import math

def find_next_square(sq):
    return (math.sqrt(sq) + 1)**2 if math.sqrt(sq).is_integer() else -1

print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))
print(find_next_square(319225))
print(find_next_square(15241383936))