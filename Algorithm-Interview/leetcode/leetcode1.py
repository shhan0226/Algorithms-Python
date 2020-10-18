import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *





# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums) - 1):
#             #print (nums[i])
#             j = i + 1
#             print (j)
#             if (nums[i] + nums[j]) == target:
#                 return [i, i + 1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


if __name__ == '__main__':
    so1 = Solution()
    li = so1.twoSum([3, 3, 1], 6)
    print(li)