#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crabGraphs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER t
#  3. 2D_INTEGER_ARRAY graph
#


def crabGraphs(n, t, graph):
  # Write your code here
  # visited = [[False] for _ in range(m+1)]
  cnn = {x: [] for x in range(1, n + 1)}

  for u, v in graph:
    cnn[u].append(v)
    cnn[v].append(u)

  nodes = set()

  for g in sorted(cnn, key=lambda x: len(cnn[x]), reverse=True):
    if g not in nodes and len(cnn[g]) >= t:
      nodes.add(g)

  for g in sorted(cnn, key=lambda x: len(cnn[x]), reverse=True):
    feet_to_fu = 0
    for v in cnn[g]:
      if v not in nodes and feet_to_fu < t:
        nodes.add(v)
        feet_to_fu += 1
  return len(nodes)


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  c = int(input().strip())

  for c_itr in range(c):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    graph = []

    for _ in range(m):
      graph.append(list(map(int, input().rstrip().split())))

    result = crabGraphs(n, t, graph)

    fptr.write(str(result) + '\n')

  fptr.close()
