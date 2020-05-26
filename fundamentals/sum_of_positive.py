# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

print(positive_sum([1,-4,7,12]))
print(positive_sum([-2,-4,-8,-12]))
print(positive_sum([]))

print('#' * 99)

# use a generator expression to create an iterator of positive numbers then pass it to the sum built-in function
def positive_sum(arr):
    return sum(x for x in arr if x>0)  

print(positive_sum([1,-4,7,12]))
print(positive_sum([-2,-4,-8,-12]))
print(positive_sum([]))

print('#' * 99)

# use lambda expression with filter higher order function to return an iterator with positive numbers only then pass them to sum built-in function
# filter is a higher order built-in function that takes in a function and an iterable as arguments and returns an iterator with the elements from the iterable for which the function returns True
def positive_sum(arr):
    return sum(filter(lambda x: x>0 ,arr))  

print(positive_sum([1,-4,7,12]))
print(positive_sum([-2,-4,-8,-12]))
print(positive_sum([]))

print('#' * 99)

# use lambda expression with map higher order function to return an iterator that applies the function to every element in the array then pass it to the sum built-in function
# map() is a higher order built-in function that takes in a function and an iterable as arguments and returns an iterator that applies the function to every element in the iterable
def positive_sum(arr):
    return sum(map(lambda x: x if x>0 else 0, arr))  

print(positive_sum([1,-4,7,12]))
print(positive_sum([-2,-4,-8,-12]))
print(positive_sum([]))

print('#' * 99)