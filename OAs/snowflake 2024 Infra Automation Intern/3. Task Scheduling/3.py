#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER_ARRAY time
#

def helper(i, j, cost, time):
    if i == len(cost):
        return [float('inf'), 0][j>=0]
    return min(cost[i] + helper(i+1, j+time[i], cost, time), helper(i+1, j-1, cost, time))

def getMinCost(cost, time):
    # Write your code here
    return helper(0, 0, cost, time)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(input().strip())

    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    time_count = int(input().strip())

    time = []

    for _ in range(time_count):
        time_item = int(input().strip())
        time.append(time_item)

    result = getMinCost(cost, time)

    fptr.write(str(result) + '\n')

    fptr.close()
