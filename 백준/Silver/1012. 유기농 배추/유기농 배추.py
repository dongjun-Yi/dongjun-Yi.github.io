import sys

sys.setrecursionlimit(10000)
T = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny)
    return True

  return False


for _ in range(T):
  m, n, k = map(int, input().split())
  graph = [[0] * m for _ in range(n)]
  result = 0

  for _ in range(k):
    a, b = map(int, input().split())
    graph[b][a] = 1

  for i in range(n):
    for j in range(m):
      if dfs(i, j) == True:
        result += 1
  print(result)
