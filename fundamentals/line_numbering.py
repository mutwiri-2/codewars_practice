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