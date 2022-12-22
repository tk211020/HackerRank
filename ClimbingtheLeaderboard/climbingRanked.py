#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Create a mapping of scores to indices
    ranked = sorted(list(set(ranked)), reverse = True)
    score_indices = {score: i for i, score in enumerate(ranked)}

    result = []
    for score in player:
        # Use binary search to find the score's position in the ranked list
        left = 0
        right = len(ranked) - 1
        while left <= right:
            mid = (left + right) // 2
            if ranked[mid] == score:
                result.append(mid + 1)
                break
            elif ranked[mid] > score:
                left = mid + 1
            else:
                right = mid - 1
        else:
            # Score not found, insert it into the ranked list
            result.append(left + 1)
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

