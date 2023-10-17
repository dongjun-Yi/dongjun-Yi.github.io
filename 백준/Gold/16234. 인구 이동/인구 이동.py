import math
from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())

graph = list()
for i in range(n):
  graph.append(list(map(int, input().split())))


def bfs(i, j):
  q = deque()
  q.append((i, j))
  visited[i][j] = True

  # 연합된 국가 담기
  union = [(i, j)]
  count = graph[i][j]  # 총 연합된 국가 수

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if visited[nx][ny]:
        continue
      if l <= abs(graph[nx][ny] -
                  graph[x][y]) <= r:  # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기
        union.append((nx, ny))
        visited[nx][ny] = True
        q.append((nx, ny))
        count += graph[nx][ny]
  # 2. 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산
  for x, y in union:
    graph[x][y] = math.floor(count / len(union))

  return len(union)


result = 0
while True:
  visited = [[False] * n for _ in range(n)]
  flag = False

  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        if bfs(i, j) > 1:
          flag = True
  if not flag:
    break
  result += 1

print(result)
