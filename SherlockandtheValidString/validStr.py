#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    counter = list(Counter(Counter(s).values()).values())
    if len(counter) > 2:
        return "NO"
    elif len(counter) == 2 and counter[1]!=1:
            return "NO"    
    return "YES" 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

