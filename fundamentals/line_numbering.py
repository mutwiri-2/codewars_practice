# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples:

# number([]) # => []
# number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]

def number(lines):
    list = []
    for index, line in enumerate(lines):
        # print(str(index+1) +': ' + line)
        list.append(str(index+1) +': ' + line)
    return list
print(number(["a", "b", "c"]))
print(number([]))

print('#' * 99)

def number(lines):
    numbered_list = []
    for index, line in enumerate(lines, 1):
        numbered_list.append("{}: {}".format(index, line))
    return numbered_list

print(number(["a", "b", "c"]))
print(number([]))
import string
print(number(list(string.ascii_letters)))


print('#' * 99)

# solution using list comprehension
def number(lines):
    numbered_list = [f"{line_number}: {line}" for line_number, line in enumerate(lines, 1)]
    return numbered_list

print(number(["a", "b", "c"]))
print(number([]))
import string
print(number(list(string.ascii_letters)))