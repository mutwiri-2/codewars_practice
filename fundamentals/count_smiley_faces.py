# Description:
# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :]

# Example cases:

# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

# Note: In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same

def count_smileys(arr):
    count = 0
    for element in arr:
        length = len(element)
        if length <=3:
            if length == 2 and (element[0] in ':;' and element[-1] in ')D'):
                count += 1
            elif length == 3 and (element[0] in ':;' and element[-1] in ')D' and element[1:-1] in '-~'):
                count += 1
    return count

print(count_smileys([]))
print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([':)',':(',':D',':O',':;']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

print('#' * 99)


def count_smileys(arr):
    count = 0
    smileys = [":)", ";)", ":~)", ";~)", ":-)", ";-)", ":D", ";D", ":~D", ";~D", ":-D", ";-D"]
    for i in arr:
      if i in smileys:
        count += 1
    return count

print(count_smileys([]))
print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([':)',':(',':D',':O',':;']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

print('#' * 99)


def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count

print(count_smileys([]))
print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([':)',':(',':D',':O',':;']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

print('#' * 99)

# best solution
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

print(count_smileys([]))
print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([':)',':(',':D',':O',':;']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))