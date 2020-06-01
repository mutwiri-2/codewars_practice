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