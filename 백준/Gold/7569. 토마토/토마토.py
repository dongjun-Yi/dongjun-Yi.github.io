import sys
from collections import deque

m, n, h = map(int, input().split())
graph = []
q = deque()

for i in range(h):
  tmp = []
  for j in range(n):
    tmp.append(list(map(int, sys.stdin.readline().split())))
    for k in range(m):
      if tmp[j][k] == 1:
        q.append((i, j, k))
  graph.append(tmp)

# 상하좌우 + 위 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
  while q:
    cur = q.popleft()
    for i in range(6):
      nx = cur[0] + dx[i]
      ny = cur[1] + dy[i]
      nz = cur[2] + dz[i]

      if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
        continue

      if graph[nx][ny][nz] == 0:
        graph[nx][ny][nz] = graph[cur[0]][cur[1]][cur[2]] + 1
        q.append((nx, ny, nz))


bfs()
res = 0

for i in graph:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    res = max(res, max(j))

print(res - 1)
