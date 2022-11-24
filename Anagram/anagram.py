#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s) % 2 == 1:
        return -1
    else:
        back = []
        counter = 0 
        for i in s[round(len(s)/2):]:
                back.append(i)

        for j in s[:round(len(s)/2)]:
            if j in back:
                back.remove(j)
            else: 
                counter += 1




        return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
