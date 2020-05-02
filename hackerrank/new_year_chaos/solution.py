#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = {x+1: 0 for x in range(len(q))}
    lbad, i = 0, 1
    while lbad < len(q)-1:
        if q[i] < q[i-1]:
            bribes[q[i-1]] += 1
            if bribes[q[i-1]] > 2:
                print('Too chaotic')
                return
            else:
                tmp = q[i]
                q[i] = q[i-1]
                q[i-1] = tmp
                i = max(1, lbad+1-10)
        else:
            if q[i] == q[i-1]+1 and lbad == i-1:
                lbad = i
            i += 1
    print(sum(bribes.values()))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
