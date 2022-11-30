#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    # The way I refer to, and the complexity is O(n)
    counter = 0
    oriQ = [x for x in range(1,len(q)+1)]
    for i in range(len(q)):
        if q[i]==oriQ[i]:
            continue
        elif q[i]==oriQ[i+1]:
            oriQ[i], oriQ[i+1] = oriQ[i+1], oriQ[i]
            counter += 1
        elif q[i]==oriQ[i+2]:
            oriQ[i+2], oriQ[i+1] = oriQ[i+1], oriQ[i+2]
            oriQ[i+1], oriQ[i] = oriQ[i], oriQ[i+1]
            counter += 2
        else:
            print("Too chaotic")
            return
    print(counter)    
    

def myMinimumBribes(q):
    # Time limit exceeded for case 6~9
    bribeList = []
    counter = 0
    for i in range(1,len(q)+1):
        if (q[i-1]-i)>=3 :
            print("Too chaotic")
            return
        for j in range(i,len(q)+1):
            if q[i-1]>q[j-1]: counter += 1
    print(counter) 
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

