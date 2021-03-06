# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
# Example:
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0

# Notes:

# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative(number):
    if number==0 or number<0:
        return number
    else:
        return -(number)  
print(make_negative(1), -1)
print(make_negative(-5), -5)
print(make_negative(0),0)


# more succint solution
# using the built-in function abs() which returns the absolute value of the argument(value of argument without a sign), then we negate the answer.
def make_negative(num):
    return -abs(num)

# another solution using ternary conditional operator --> a if condition else b
#Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single line replacing the multiline if-else making the code compact. - https://www.geeksforgeeks.org/ternary-operator-in-python/
def make_negative( number ):
    return -number if number>0 else number

print(make_negative(1), -1)
print(make_negative(-5), -5)
print(make_negative(0),0)