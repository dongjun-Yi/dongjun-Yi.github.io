import sys
from collections import deque


def bfs(v):
  q = deque([v])
  while q:
    v = q.popleft()
    if v == k:
      return arr[v]

    for x in (v - 1, v + 1, v * 2):
      if 0 <= x < MAX and not arr[x]:
        arr[x] = arr[v] + 1
        q.append(x)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
arr = [0] * MAX
print(bfs(n))
