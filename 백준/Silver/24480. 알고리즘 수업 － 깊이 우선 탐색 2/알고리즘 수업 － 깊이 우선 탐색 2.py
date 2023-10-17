import sys

sys.setrecursionlimit(1000000000)

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)


def DFS(x):
  global cnt
  visited[x] = True
  res[x] = cnt
  graph[x].sort(reverse=True)

  for k in graph[x]:
    if visited[k] == False:
      cnt += 1
      DFS(k)


res = [0] * (n + 1)

cnt = 1

DFS(r)

for i in range(1, len(res)):
  print(res[i])
