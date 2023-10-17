from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)


def bfs(x):
  global cnt
  q = deque([x])
  visited[x] = True

  while q:
    cur = q.popleft()

    for v in graph[cur]:
      if not visited[v]:
        visited[v] = True
        cnt += 1
        q.append(v)


res = []
for i in range(1, n + 1):
  visited = [False] * (n + 1)
  cnt = 0
  bfs(i)
  res.append(cnt)

largest = max(res)

for i in range(len(res)):
  if res[i] == largest:
    print(i + 1, end=' ')