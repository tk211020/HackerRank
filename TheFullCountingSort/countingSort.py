#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    result = []
    resultStr = ''
    for i in range((len(arr)//2)+1):
        result.append([])
    for i in range(len(arr)):
        if i < (len(arr)//2):
            result[int(arr[i][0])].append('-')
        else:
            result[int(arr[i][0])].append(arr[i][1])
            
    for i in result:
        for j in i :
            print(j,end=" ")
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
