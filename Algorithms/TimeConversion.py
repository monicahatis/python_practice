#!/bin/python3
'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    hour = int(s[:2])
    minute = int(s[3:5])
    sec = int(s[6:8])
    am_pm = s[-2:]

    # Convert to 24-hour clock
    if am_pm == 'AM':
        if hour == 12:
            hour = 0
    elif am_pm == 'PM':
        if hour != 12:
            hour += 12
    # format the 24 hour time
    return '{:02d}:{:02d}:{:02d}'.format(hour, minute, sec)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
