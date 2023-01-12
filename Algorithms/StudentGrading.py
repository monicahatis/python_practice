#!/bin/python3
'''
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from 0 to 100 .
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of grade is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
'''

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] >= 38:
            if (grades[i] // 5) * 5 + 5 - (grades[i] )  < 3:
                grades[i] = (grades[i] // 5) * 5 + 5
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()