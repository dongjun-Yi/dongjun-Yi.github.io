from collections import deque

m, n = map(int, input().split())

graph = []
for _ in range(m):
  a = list(map(str, input()))
  graph.append(list(map(int, a)))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for i in range(n)] for _ in range(m)]


def bfs(x, y):
  q = deque([(x, y)])
  visited[x][y] = True
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append((nx, ny))


for i in range(n):
  if graph[0][i] == 0 and visited[0][i] == False:
    bfs(0, i)

res = "NO"

for end in range(n):
  if visited[-1][end]:
    res = "YES"
    break

print(res)
