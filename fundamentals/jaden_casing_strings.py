# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
# example
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

# my solution
def to_jaden_case(string):
    return ' '.join([word[0].upper() + word[1:] for word in string.split()])
    
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


print('#' * 99)
# I initially used the title() method but it failed the test cases because from the documentation- The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions and possessives form word boundaries, which may not be the desired result

#  refer to the following stack overflow answer https://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string

def to_jaden_case(string):
    return string.title()

print("Solution using title() method")
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

print('#' * 99)
# I then had to use list comprehensions to solve it. First get a list of the words in the string using split() then loop over every word in the list capitalize the first letter and append the rest of the letters. Then call the join string method using space as the delimiter to create a string from the words which you return as the output
# The expression [word[0].upper() + word[1:] in the list comprehension can be replaced by the capitalize string method which returns a capitalized version of a word, i.e. make the first character have upper case and the rest lower case like so

def to_jaden_case(string):
    return ' '.join([word.capitalize() for word in string.split()])

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
