import sys

n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

# 이동방향
dx = [1, 1, 1]
dy = [-1, 0, 1]

route = [0] * n

res = sys.maxsize


def dfs(L, x, y, direction):
  global res
  if L == (n - 1):
    if res > sum(route):
      res = sum(route)
  else:
    for i in range(3):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if not visited[nx][ny] and direction != dy[i]:
        visited[nx][ny] = True
        route[L + 1] = graph[nx][ny]
        dfs(L + 1, nx, ny, dy[i])
        visited[nx][ny] = False


for i in range(m):
  visited = [[False] * m for _ in range(n)]
  visited[0][i] = True
  route[0] = graph[0][i]
  dfs(0, 0, i, 2)

print(res)
