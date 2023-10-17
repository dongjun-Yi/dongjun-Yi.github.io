#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
  # Write your code here
  ranked = sorted(set(ranked), reverse=True)
  res = []
  rank = len(ranked) - 1

  for p in player:

    while rank >= 0 and ranked[rank] <= p:
      rank -= 1
    if rank < 0:
      res.append(1)
      continue
    res.append(rank + 2)

  return res


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  ranked_count = int(input().strip())

  ranked = list(map(int, input().rstrip().split()))

  player_count = int(input().strip())

  player = list(map(int, input().rstrip().split()))

  result = climbingLeaderboard(ranked, player)

  fptr.write('\n'.join(map(str, result)))
  fptr.write('\n')

  fptr.close()
