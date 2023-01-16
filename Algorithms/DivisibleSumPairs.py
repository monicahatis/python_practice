#!/bin/python3
'''
Given an array of integers and a positive integer k, determine the number of (i, j) pairs where i <j  and  arr[i]+arr[j]  is divisible by k.

Example
ar=[1,2,3,4,5,6]
k=5

Three pairs meet the criteria:[1,4], [2,3] and [4,6].
'''

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, arr):
    # Write your code here
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()