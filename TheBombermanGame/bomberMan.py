#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n == 0 or n ==1:
        pass
    elif n % 2 == 0:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i]= grid[i][:j]+"O"+grid[i][j+1:] 
    elif n % 4 == 1:
            grid = detonate(detonate(grid))
    elif n % 4 == 3:
        grid = detonate(grid)
    return grid
def detonate(grid):
    r = len(grid)
    c = len(grid[0])
    nextState = ["O"*c for i in range(r)]
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="O": 
                    nextState[i] =  nextState[i][:j] + "." + nextState[i][j+1:]
                    if i!=0:    
                        #nextState[i-1][j] = "."
                        nextState[i-1] = nextState[i-1][:j]+"."+nextState[i-1][j+1:]
                    if i!=(r-1): 
                       #nextState[i+1][j] = "."
                        nextState[i+1] = nextState[i+1][:j]+"."+nextState[i+1][j+1:]
                    if j!=0: 
                        #nextState[i][j-1] = "."
                        nextState[i] = nextState[i][:j-1]+"."+nextState[i][j:]
                    if j!=(c-1): 
                        #nextState[i][j+1] = "."
                        nextState[i] = nextState[i][:j+1]+"."+nextState[i][j+2:]
    return nextState
  
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

