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


    