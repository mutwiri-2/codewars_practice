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

def count_smileys(arr):
    count = 0
    for element in arr:
        if element[0] in ':;' and element[-1] in ')D':
            if element[1:-1] == [] or '-~' in element[1:-1]:
                count+=1
    return count



print(count_smileys([]))
print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([':)',':(',':D',':O',':;']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))