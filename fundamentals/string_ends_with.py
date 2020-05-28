# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    return ending in string[-len(ending):]

print(solution('abcde', 'cde'))
print(solution('abcde', 'abc'))
print(solution('abcde', ''))

# another solution
#startswith() and endswith() string methods return True if the string they are called on starts with or ends with the string passed to the methods. They are a good alternative to the '==' operator if you just want to check just the equality of the first or last parts of a string rather than the whole string. It is a case sensitive comparison
def solution(string, ending):
    return string.endswith(ending)

print(solution('abcde', 'cde'))
print(solution('abcde', 'abc'))
print(solution('abcde', ''))