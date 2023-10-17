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
      print(abs(heapq.heappop(q)))
  else:
    heapq.heappush(q, -s)
