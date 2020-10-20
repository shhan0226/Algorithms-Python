#!/bin/python3

import os
import sys
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(nums):
    #
    # Write your code here.
    #
    bin_num: Deque = collections.deque()

    for num in nums:
        bin_num.append()



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    nums_count = int(input())

    nums = []

    for _ in range(nums_count) :
        nums_item = int(input().strip())
        nums.append(nums_item)


    result = simpleArraySum(nums)

    fptr.write(str(result) + '\n')

    fptr.close()
