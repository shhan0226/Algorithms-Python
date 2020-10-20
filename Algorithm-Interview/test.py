import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


if __name__ == '__main__':
    # so1 = Solution()
    # li = so1.twoSum([3, 3, 1], 6)
    # print(li)

    strs: Deque = collections.deque()

    strs.append("123")
    strs.append("123")
    strs.append("123")
    # print(type(strs))
    # print(strs)
    A = strs.popleft()
    # print(A)

    strs2 = "123456"
    print(strs2)
    strs2 = strs2[::-1]
    print(strs2)

    #re.sub('패턴', 교체함수, '문자열', 바꿀횟수)

    nums = [0, 1, 0, 1]

    bin_num = collections.defaultdict(list)
    ex_num = {}

    su: int
    result =[]

    #
    for i, num in enumerate(nums):
        ex_num[i] = num
        bin_num[i] = bin(num).count('1')

    bin_num = sorted(bin_num.items(), key=lambda x: x[1])
    print(bin_num)

    for tu in bin_num:
        result.append(nums[ list(tu)[0]])
        print(nums[list(tu)[0]])

    print(result)



    # for key, val in bin_num.items():
    #     print(num[key])
