#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    ans = 0
    for l in range(1, len(s)+1):
        occ = defaultdict(int)
        for i in range(len(s)-l+1):
            occ[''.join(sorted(list(s[i:i+l])))] += 1
        for k, v in occ.items():
            ans += v*(v-1)/2
    return int(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
