# The main idea is to count all the occurring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

# What if the string is empty ? Then the result should be empty object literal { }

# For C#: Use a Dictionary<char, int> for this kata!

def count(string):
    result = {}
    for char in string:
        result[char] = result.get(char,0) + 1
    return result

print(count('aba'))
print(count(''))

print('#' * 99)

# alternate solution
def count(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.setdefault(char, 0) + 1
    return char_count
print(count('aba'))
print(count(''))

print('#' * 99)

# alternate solution
def count(string):
    return {i: string.count(i) for i in string}

print(count('aba'))
print(count(''))

print('#' * 99)

# alternate solution - using Counter from collections module 
# A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts

from collections import Counter

def count(string):
    return dict(Counter(string))

print(count('aba'))
print(count(''))

print('#' * 99)
# alternate solution - use set to get unique elements in string - then get the count of each unique element

def count(string):
    result = {}
    for char in set(string):
        result[char] = string.count(char)
    return result 

print(count('aba'))
print(count(''))

print('#' * 99)