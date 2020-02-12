# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Divison should be integer division. For example, this should return 2, not 2.666666... :
# eight(divided_by(three()))

def zero():
    return 0 #your code here
def one():
    return 1 #your code here
def two():
    return 2 #your code here
def three():
    return 3 #your code here
def four():
    return 4 #your code here
def five():
    return 5 #your code here
def six():
    return 6 #your code here
def seven():
    return 7 #your code here
def eight():
    return 8 #your code here
def nine():
    return 9 #your code here

print(zero())

def plus(num):
    return eval('+') #your code here
def minus(num):
    return eval('-') #your code here
def times():
    return  
def divided_by(num):
    return eval('//') #your code here

print(seven(times(five())))