#!/bin/python3
'''
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Example
arr =[1,1,2,2,3]
There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1. 
'''

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    bird_count = {}
    for bird in arr:
        if bird in bird_count:
            bird_count[bird] += 1
        else:
            bird_count[bird] = 1
    
    # Find the maximum count of bird sightings
    max_count = max(bird_count.values())
    
    # Find the bird type(s) with the maximum count and store them in a list
    max_birds = [bird for bird, count in bird_count.items() if count == max_count]
    
    # Sort the list of max_birds and return the smallest id
    return min(max_birds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()