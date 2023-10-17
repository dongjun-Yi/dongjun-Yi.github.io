import sys

sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
  global area
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  if graph[x][y] == 1:
    area += 1
    graph[x][y] = 0
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False


res = 0
cnt = 0

for i in range(n):
  for j in range(m):
    area = 0
    if dfs(i, j):
      if res < area:
        res = area
      cnt += 1

print(cnt)
print(res)