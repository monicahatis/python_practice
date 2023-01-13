#!/bin/python3
'''
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
'''

import math
import os
import random
import re
import sys
from math import gcd
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    lcm_a = a[0]
    gcd_b = b[0]
    for i in range(1, len(a)):
        lcm_a = lcm(lcm_a, a[i])
    for i in range(1, len(b)):
        gcd_b = gcd(gcd_b, b[i])

    count = 0
    for i in range(lcm_a, gcd_b+1, lcm_a):
        if gcd_b % i == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
