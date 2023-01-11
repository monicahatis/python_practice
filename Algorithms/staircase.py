#!/bin/python3
#Write a program that prints a staircase of size n.

import math
import os
import random
import re
import sys


# The function accepts INTEGER n as parameter.

def staircase(n):
    # The loop variable i is being defined in the range 1 to n+1 by for i in range(1, n + 1)
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)
        """ 
        #This line contains two parts:
' ' * (n - i) creates a string of spaces that is n - i characters long. The number of spaces decreases as the loop variable i increases.
'#' * i creates a string of # characters that is i characters long. The number of # characters increases as the loop variable i increases.
These two parts are then concatenated using the + operator, resulting in a string that has n - i spaces followed by i # characters.
Finally, the print() function is called with this string as an argument, causing the string to be printed to the console.
So overall it prints a stair case with n levels, and the spaces before the # decreases as the the stair level increases.
"""
        
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)