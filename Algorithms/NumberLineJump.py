#!/bin/python3
'''
You are choreographing a circus show with various animals.
 For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
If it is possible, return YES, otherwise return NO.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    '''
    First, the function checks if the second kangaroo's velocity is greater than or equal to the first kangaroo's velocity.
     If this is the case, it's impossible for the first kangaroo to catch up to the second kangaroo, so it returns "NO"
    '''
    if v2 >= v1:
        return "NO"
    '''
Otherwise, the function checks whether the difference in position between the two kangaroos is divisible by the difference in velocity between the two kangaroos.
(x2 - x1) % (v1 - v2) == 0 is used to check the divisibility, here the % is modulus operator, it returns the remainder of the division of x2-x1 by v1-v2.
If the difference in position is divisible by the difference in velocity, it means that the two kangaroos will meet at the same location at the same time.
 In this case, the function returns "YES".
    '''
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
