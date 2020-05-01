#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    from_to= defaultdict(list)
    for i in range(t_edges):
        from_to[t_to[i]].append(t_from[i])

    forests = []
    def getForests(node):
        if len(from_to[node]) == 0:
            return 1
        child_sum = sum(getForests(x) for x in from_to[node])
        if (child_sum+1)%2 == 0:
            forests.append(1)
            return 0
        return child_sum+1
    getForests(1)
    return len(forests)-1
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
