#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def MiMaSum(arr):
    # Write your code here
    arr_sum = sum(arr)
    print(arr_sum - max(arr), arr_sum - min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    MiMaSum(arr)