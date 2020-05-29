# Task
# Given a string str, reverse it omitting all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# Input/Output
# [input] string str

# A string consists of lowercase latin letters, digits and symbols.

# [output] a string

def reverse_letter(string):
    string_list = []
    reversed_string = string[::-1]
    # print(reversed_string)
    import string
    for i in range(0, len(reversed_string)):
        # print(reversed_string[i])
        if reversed_string[i] in string.ascii_lowercase:
            string_list.append(reversed_string[i])
    return ''.join(string_list)

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))

print('#' * 99)

def reverse_letter(string):
    return ''.join([i for i in string[::-1] if i.isalpha()])

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))


print('#' * 99)
# use filter higher-order function passing it <method 'isalpha' of 'str' objects> (str.isalpha) and the reversed version of the passed string. This returns an iterator of all elements in the reversed string that are alphabets then calling join string method on them returns a string

def reverse_letter(string):
    return ''.join(filter(str.isalpha, reversed(string)))

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))

    
print('#' * 99)
# use regexes - find all occurrences of alphabets and then reverse that list and create a string using join
import re
def reverse_letter(string):
    return "".join(re.findall(r"[a-zA-Z]", string)[::-1])
    

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))