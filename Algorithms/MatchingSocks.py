#!/bin/python3
''''
There is a large pile of socks that must be paired by color.
 Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # Create a dictionary to store the count of each color
    color_count = {}
    for color in ar:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    # Initialize a variable to store the number of pairs
    pairs = 0
    # Iterate through the dictionary and add the floor of count of each color divided by 2 to the pairs variable
    for count in color_count.values():
        pairs += count // 2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
