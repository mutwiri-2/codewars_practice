# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
# should return "found the needle at position 5"

def find_needle(haystack):
    for index, key in enumerate(haystack):
      if key == 'needle':
          return "found the needle at position {}".format(index)

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

print('#' * 99)
# more succint solution
# The index() method searches an element in the list and returns its index. In simple terms, the index() method finds the given element in a list and returns its position. If the same element is present more than once, the method returns the index of the first occurrence of the element
def find_needle(haystack):
  return 'found the needle at position {}'.format(haystack.index('needle'))

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))


print('#' * 99)

# using f strings
def find_needle(haystack):
  return f'found the needle at position {haystack.index("needle")}'

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

print('#' * 99)

# using string concatenation
def find_needle(haystack):
  return 'found the needle at position ' +  str(haystack.index("needle"))

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))