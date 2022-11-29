#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    b=[]
    m = 0
    for i in range(len(a)):
        b.append([])
        for j in range(len(a)):
            b[i].append(a[j]-a[i])
    for i in range(len(b)):
            if(b[i].count(-1)+b[i].count(0)>m):
                m = b[i].count(-1)+b[i].count(0)
            if(b[i].count(1)+b[i].count(0)>m):
                m = b[i].count(1)+b[i].count(0)
    return(m)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

