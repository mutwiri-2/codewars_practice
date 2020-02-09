# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, and u as vowels for this Kata.

# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    for letter in input_str:
        if letter in ('a','e','i','o','u'):
            num_vowels += 1
    
    return num_vowels

print(get_count('learn by practice the github pull request workflow'))
print(get_count('fork this template for the 100 days journal - to keep yourself accountable (multiple languages available)'))
print(get_count('solutions from my python3 code practice challenges from hackerrank'))
print(get_count('code practice from my freecodecamp study'))

# more succint solution

def vowels_count(s):
    return sum(i in 'aeiou' for i in s)

print(vowels_count('Seeing something unexpected? Take a look at the GitHub profile guide.'))


