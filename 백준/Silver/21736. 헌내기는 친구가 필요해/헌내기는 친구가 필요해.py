import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = []
visited = [[0] * m for _ in range(n)]

for i in range(n):
  graph.append(list(input()))
  for j in range(m):
    if graph[i][j] == 'I':
      start = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def dfs(x, y):
  global cnt

  visited[x][y] = 1

  if graph[x][y] == 'P':
    cnt += 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if graph[nx][ny] != 'X' and not visited[nx][ny]:
      dfs(nx, ny)


dfs(start[0], start[1])

if cnt:
  print(cnt)
else:
  print("TT")
