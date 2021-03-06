# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example:

#  persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.

#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.

#  persistence(4) => 0   # Because 4 is already a one-digit number.


def persistence(n):
    times = 0
    product = 1
    while len(str(n)) != 1:
        for i in list(str(n)):
            product *= int(i)
        n = product
        product = 1
        times += 1
    return times

print(persistence(4))
print(persistence(39))
print(persistence(999))
print(persistence(3456))

print('#' * 99)
# second solution - similar to first 

def persistence(n):
    count = 0
    while len(str(n)) != 1:
        count += 1
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
    return count

print(persistence(4))
print(persistence(39))
print(persistence(999))
print(persistence(3456))


print('#' * 99)
