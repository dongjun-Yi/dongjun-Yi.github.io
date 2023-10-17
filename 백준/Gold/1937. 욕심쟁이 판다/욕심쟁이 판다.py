import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
  if visited[x][y]:
    return visited[x][y]

  visited[x][y] = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      continue
    if graph[nx][ny] > graph[x][y]:
      visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)

  return visited[x][y]


cnt = 0
for i in range(n):
  for j in range(n):
    cnt = max(cnt, dfs(i, j))

print(cnt)
