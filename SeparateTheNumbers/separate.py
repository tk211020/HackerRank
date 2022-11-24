#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    for i in range(1, len(s) // 2 + 1):
        num = s[:i]
        valid_s = num
        count = 1
        while len(valid_s) < len(s):
            next_num = int(num) + count
            valid_s += str(next_num)
            count += 1
        if valid_s == s:
            print(f'YES {num}')
            return
    print('NO')
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

