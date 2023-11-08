#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER wordLen
#  2. INTEGER maxVowels
#

def calculateWays(wordLen, maxVowels):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    wordLen = int(input().strip())

    maxVowels = int(input().strip())

    result = calculateWays(wordLen, maxVowels)

    fptr.write(str(result) + '\n')

    fptr.close()
