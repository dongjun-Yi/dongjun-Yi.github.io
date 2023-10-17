import sys

n = int(input())

a, b = map(int, input().split())

k = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(k):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)


def dfs(L, x):
  if x == b:
    print(L)
    sys.exit(0)
  else:
    for v in graph[x]:
      if not visited[v]:
        visited[v] = True
        dfs(L + 1, v)


dfs(0, a)
print(-1)