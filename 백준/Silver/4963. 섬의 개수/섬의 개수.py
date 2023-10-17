# 섬의 개수 : 대각선으로도 섬으로 한 섬으로 판정하여 상하좌우 대가선을 체크해줘야함

import sys

sys.setrecursionlimit(100000)

# 상하좌우 좌대각선, 우대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(x, y):
  # 해당 노드의 방문처리를 해줘야 함
  if graph[x][y] == 0:
    return False
  graph[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= m or ny < 0 or ny >= n:
      continue
    if graph[nx][ny] == 0:
      continue
    if graph[nx][ny] == 1:
      dfs(nx, ny)
  return True


while True:
  cnt = 0
  graph = []
  n, m = map(int, input().split())
  visited = [[False] * n for _ in range(m)]
  if n == 0 and m == 0:
    break
  for _ in range(m):
    graph.append(list(map(int, input().split())))

  for i in range(m):
    for j in range(n):
      if dfs(i, j):
        cnt += 1
  print(cnt)
