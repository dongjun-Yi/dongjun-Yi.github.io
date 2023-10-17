import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

visited = [False] * n

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


def dfs(L, x):
  if L == 4:
    print(1)
    sys.exit(0)
  for v in graph[x]:
    if not visited[v]:
      visited[v] = True
      dfs(L + 1, v)
      visited[v] = False


for i in range(n):
  visited[i] = True
  dfs(0, i)
  visited[i] = False

print(0)
