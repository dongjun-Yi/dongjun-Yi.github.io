from collections import deque

m, n = map(int, input().split())

graph = []
visited = [[False] * n for _ in range(m)]

for _ in range(m):
  graph.append(list(map(int, input().split())))

#상하좌우 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = True

  while q:
    x, y = q.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 1 and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append((nx, ny))


cnt = 0

for i in range(m):
  for j in range(n):
    if graph[i][j] == 1 and not visited[i][j]:
      bfs(i, j)
      cnt += 1

print(cnt)
