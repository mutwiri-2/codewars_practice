# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    num_str = str(num)
    size = len(num_str)
    result = []
    for i in range(0,size):
        if num_str[i] != '0':
            result.append(num_str[i] + '0'*((size-1)-i))
    return ' + '.join(result)

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

print('#' * 99)
# alternate solution - use a generator function to create an iterator of the expanded form of each non-zero digit in a number then join them using the + operator
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(digit + '0' * (len(num) - index - 1) for index,digit in enumerate(num) if digit != '0')
    

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

print('#' * 99)
# alternate solution - use a list comprehension to create a list of the expanded form of each non-zero digit in a number then join them using the + operator
def expanded_form(num):
    num = list(str(num))
    return ' + '.join([digit + '0' * (len(num) - index -1) for index, digit in enumerate(num) if digit != '0'])


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))