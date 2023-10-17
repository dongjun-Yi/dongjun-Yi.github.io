import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n + 1)
cnt = 0


def dfs(x):
  visited[x] = True
  for v in graph[x]:
    if not visited[v]:
      dfs(v)


for i in range(1, n + 1):
  if not visited[i]:
    dfs(i)
    cnt += 1

print(cnt)