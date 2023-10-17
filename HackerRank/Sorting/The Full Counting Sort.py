#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
  # Write your code here
  half = len(arr) // 2
  res = [[i] for i in range(len(arr))]

  for i in range(half):
    res[int(arr[i][0])].append('-')

  for i in range(half, len(arr)):
    res[int(arr[i][0])].append(arr[i][1])

  s = ''
  for i in range(len(res)):
    for j in range(1, len(res[i])):
      s += str(res[i][j]) + ' '
  print(s)


if __name__ == '__main__':
  n = int(input().strip())

  arr = []

  for _ in range(n):
    arr.append(input().rstrip().split())

  countSort(arr)
