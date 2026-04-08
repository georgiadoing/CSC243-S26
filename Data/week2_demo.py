#############################################
# Georgia Doing (doingg@union.edu)
# partner, group:
# 4/8/26
''' In class function demos
 described in a long comment'''
#############################################

# import statements / constants
A = 5
import random

# function definitions

def say_hi():
    print('Hi')

def say_hello(name):
    print('Hi ' + name)

def merge(thing1, thing2):
    print('merge:', thing1 + thing2)

def length(something):
    print('Length of', something, 'is', len(something))

# main function
def main():
    # example of pretty printing
    length('Ginny')
    # int addition
    merge(1,2)
    # string concatenation
    merge('Hi ', 'Ginny')
    #say_hello('Ginny')
    
# function call - main()
main()
