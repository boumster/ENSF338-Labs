# Code takes a number argument and checks if it is a prime number
# if it is a prime number prints yes, otherwise prints no
# The error in the code was in the print('Yes`) as it did not have matching quotation marks

import sys
def do_stuff():
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print('No')
                return
        print('Yes')
# Test the function
do_stuff()