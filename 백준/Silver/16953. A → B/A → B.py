import sys
from collections import deque

a, b = map(int, input().split())


def bfs(x):
  cnt = 0
  q = deque([(x, cnt)])

  while q:
    cur = q.popleft()
    if int(cur[0]) == b:
      print(cur[1] + 1)
      sys.exit(0)
    if int(cur[0]) > b:
      continue
    q.append((int(cur[0]) * 2, cur[1] + 1))
    q.append((str(cur[0]) + '1', cur[1] + 1))

  print(-1)


bfs(a)