import sys

sys.setrecursionlimit(10000)
n = int(input())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))


def dfs(x):
  for i in range(n):
    if graph[x][i] == 1 and visited[i] == 0:
      visited[i] = 1
      dfs(i)


for x in range(n):
  visited = [0 for _ in range(n)]
  dfs(x)
  print(*visited)
