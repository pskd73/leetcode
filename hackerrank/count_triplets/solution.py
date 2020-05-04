#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    pt, t = defaultdict(int), defaultdict(int)
    ans = 0
    for n in arr:
        if n in t:
            ans += t[n]
        if n in pt:
            t[n*r] += pt[n]
        pt[n*r] += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
