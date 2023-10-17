from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, wall):
  q = deque([(x, y, wall)])

  visited[x][y][wall] = 1

  while q:
    x, y, wall = q.popleft()
    if x == n - 1 and y == m - 1:
      return visited[n - 1][m - 1][wall]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
        q.append((nx, ny, wall))
        visited[nx][ny][wall] = visited[x][y][wall] + 1

      if graph[nx][ny] == 1 and wall == 1:
        q.append((nx, ny, wall - 1))
        visited[nx][ny][wall - 1] = visited[x][y][wall] + 1
  return -1


print(bfs(0, 0, 1))
