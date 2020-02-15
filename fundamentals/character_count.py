# The main idea is to count all the occurring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

# What if the string is empty ? Then the result should be empty object literal { }

# For C#: Use a Dictionary<char, int> for this kata!

def count(string):
    result = {}
    for char in list(string):
        result[char] = result.get(char,0) + 1
    return result

# alternate solution
def count(string):
    return {i: string.count(i) for i in string}

print(count('aba'))
print(count(''))
