# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# solution("camelCasing")  ==  "camel Casing"

def solution(s):
    import string
    s_list = list(s)
    result = ''
    uppercase_letters_count = 0
    for letter in s_list:
        if letter in string.ascii_uppercase:
            uppercase_letters_count+=1
    for i in range(0,uppercase_letters_count):
        for index, letter in enumerate(s_list):
            if letter in string.ascii_uppercase:
                s_list = s_list[:index+i] + [' '] + s_list[index+i:]
    for letter in s_list:
        result+=letter
    return result








print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
