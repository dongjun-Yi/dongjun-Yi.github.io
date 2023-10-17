import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
  s = int(input())

  if s == 0:
    if len(q) == 0:
      print(0)
    else:
      a, b = heapq.heappop(q)
      print(b)
  else:
    heapq.heappush(q, (abs(s), s))
