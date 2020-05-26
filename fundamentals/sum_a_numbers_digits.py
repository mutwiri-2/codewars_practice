# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:

#   sum_digits(10)  # Returns 1
#   sum_digits(99)  # Returns 18
#   sum_digits(-32) # Returns 5
# Let's assume that all numbers in the input will be integer values.

def sum_digits(number):
    number = abs(number)
    num_str = str(number)
    # print(num_str)
    sum = 0
    for i in num_str:
        # print(i)
        sum += int(i)
    return sum

print(sum_digits(10))
print(sum_digits(99))
print(sum_digits(-32))

print('#' * 99)
# more succint solution - using a generator expression return an iterator of characters in the string version of the number converted to its absolute value - then pass each to the integer function to convert it to a number then to the sum function to get the sum of all the objects in the iterator
def sum_digits(number):
    return sum(int(i) for i in str(abs(number)))

print(sum_digits(102123))
print(sum_digits(99456))
print(sum_digits(-35672))


print('#' * 99)
# another solution - using lambda function and the map() higher order function return an iterator that applies the anonymous function (which just converts it's argument to an int) to every element in the iterable then pass this to the sum function
def sum_digits(number):
    return sum(map(lambda x: int(x), str(abs(number))))

print(sum_digits(102123))
print(sum_digits(99456))
print(sum_digits(-35672))