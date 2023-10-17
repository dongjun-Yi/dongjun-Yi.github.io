from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
res = [0] * (n + 1)
visited = [False] * (n + 1)


def bfs(v):
  q = deque([v])
  visited[v] = True

  while q:
    cur = q.popleft()
    for x in graph[cur]:
      if not visited[x]:
        res[x] = cur
        q.append(x)
        visited[x] = True


for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

bfs(1)
for i in range(2, n + 1):
  print(res[i])
