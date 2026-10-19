"""
Problem: 2D Array - Hourglass Sum

Description:
Given a 6x6 2D array of integers, an "hourglass" is a subset of 7 values structured like this:
a b c
  d
e f g

There are exactly 16 hourglasses in a 6x6 grid. 

Objective:
Calculate the sum of the 7 integers for each of the 16 hourglasses and return the maximum sum.

Constraints:
- The array size is strictly 6x6.
- Matrix values range from -9 to 9.
- The maximum sum can be negative, so initialize the max sum tracker with negative infinity.


"""

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    
    max_sum = float('-inf')
    for i in range(4):
        for j in range(4):
            current_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                           arr[i+1][j+1] +
                           arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

arr = []
for _ in range(6):
  arr.append(list(map(int, input().rstrip().split())))
result = hourglassSum(arr)
print(result)

"""
sample input 
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""