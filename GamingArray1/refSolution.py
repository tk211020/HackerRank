#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    currentMax, maxCounter = arr[0], 1
    
    for i in range(len(arr)):
        if currentMax < arr[i]:
            maxCounter = maxCounter+1
            currentMax = arr[i]
    return "BOB" if (maxCounter % 2) != 0 else "ANDY"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()

