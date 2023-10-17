import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n + 1)
cnt = 0
res = [0] * (n + 1)


def bfs(v):
  global cnt
  dq = deque([v])
  visited[v] = True

  while dq:
    cur = dq.popleft()
    cnt += 1
    res[cur] = cnt
    graph[cur].sort()
    for x in graph[cur]:
      if visited[x] == False:
        dq.append(x)
        visited[x] = True


bfs(r)

for i in range(1, n + 1):
  print(res[i])
