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