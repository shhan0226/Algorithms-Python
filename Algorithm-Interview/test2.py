import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

if __name__ == '__main__':
    addresses = ['::1', '121.0.19.121', '201.0.190.071']
    addresses2 = ['::1', '2001::0000:0000:0000:0000:0000:0001', '42:0000:ff00:0000:0000:0000:0000:0001']
    addresses3 = ['123123123,123123,123123']
    for addr in addresses:

        num = addr.split('.')
        str1 = "".join(num)
        if str1 in "::1":
            print(str1)



        print(num)
        true_list = [True, True, True, True]

        if len(num) == 4:
            # num_int = list(map(int, num))

            if list(map(lambda x: 0 <= x < 255, list(map(int, num)))) == true_list:
                print("ipv4")


            continue


        else:
            print("ipv4__")

        num = addr.split(':')
        if len(num) == 8:
            print("ipv8")
            continue
        else:
            print("ipv8__")
    print("NE")

    str22 = 'AAA'
    print(str22.isalpha())











    n: int
    n = 0
    bin_n = bin(n)
    if bin_n == bin(0):
        print(bin_n)
    else:
        print("n..")
    result = int(bin_n, 2)
    print(result)



        # num = re.split("[.:]", addr)
        #
        # if len(num) == 8 :
        #
        #     print(num)
        #     print("ipv8")
        #
        # elif len(num) == 4 :
        #
        #     print(num)
        #     print("ipv4")
        # else :
        #
        #     print(num)
        #     print("Neither")

    val: int = 10
    print(val)
    print(type(val))