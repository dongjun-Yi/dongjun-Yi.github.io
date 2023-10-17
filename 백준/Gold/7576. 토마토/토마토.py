from collections import deque

m, n = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))


q = deque()

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      q.append((i, j))

bfs()
ans = 0

for row in graph:
  for tomato in row:
    if tomato == 0:
      print(-1)
      exit()
  ans = max(ans, max(row))

print(ans - 1)
