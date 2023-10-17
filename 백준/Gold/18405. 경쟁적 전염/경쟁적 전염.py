from collections import deque

n, k = map(int, input().split())
graph = []
virus = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      # 바이러스종류, 초, 위치 x, 위치 y
      virus.append((graph[i][j], 0, i, j))

s, X, Y = map(int, input().split())
virus.sort()

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque(virus)


def bfs(s, X, Y):
  while q:
    v, t, x, y = q.popleft()
    if t == s:
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = v
        q.append((v, t + 1, nx, ny))
  return graph[X - 1][Y - 1]


print(bfs(s, X, Y))
