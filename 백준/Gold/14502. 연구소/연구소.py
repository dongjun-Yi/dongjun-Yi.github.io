from collections import deque
import sys

input = sys.stdin.readline
import copy

n, m = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 바이러스 개수 세기
def bfs():
  global answer
  q = deque()
  tmp_graph = copy.deepcopy(graph)

  for i in range(n):
    for j in range(m):
      if tmp_graph[i][j] == 2:
        q.append((i, j))

  while q:
    cur = q.popleft()

    for i in range(4):
      nx = cur[0] + dx[i]
      ny = cur[1] + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if tmp_graph[nx][ny] == 0:
        tmp_graph[nx][ny] = 2
        q.append((nx, ny))

  cnt = 0
  for i in range(n):
    cnt += tmp_graph[i].count(0)

  answer = max(answer, cnt)


# 모든 경우의 수를 탐색하여 벽을 3개 세우기
def makeWall(cnt):
  if cnt == 3:
    bfs()
    return

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        makeWall(cnt + 1)
        graph[i][j] = 0


answer = 0

makeWall(0)
print(answer)
