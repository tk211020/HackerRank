#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Create a hash table to store the numbers in the array
    num_count = {}
    for i, num in enumerate(arr):
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # Find the two numbers that sum to m
    for i, num in enumerate(arr):
        complement = m - num
        if complement in num_count and (complement != num or num_count[num] > 1):
            return i + 1, arr[i+1:].index(complement) + i + 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
