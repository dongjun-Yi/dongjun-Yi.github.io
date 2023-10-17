from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for k in range(n):
  sum = 0
  a = list(map(int, input().split()))
  for i in range(0, len(a), 3):
    sum = 0
    for j in range(i, i + 3):
      sum += a[j]
    graph[k].append(int(sum // 3))

t = int(input())
cnt = 0

for i in range(n):
  for j in range(m):
    if graph[i][j] >= t:
      graph[i][j] = 255
    else:
      graph[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  q = deque([(x, y)])
  graph[x][y] = 0

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 255:
        graph[nx][ny] = 0
        q.append((nx, ny))


for i in range(n):
  for j in range(m):
    if graph[i][j] == 255:
      bfs(i, j)
      cnt += 1

print(cnt)
