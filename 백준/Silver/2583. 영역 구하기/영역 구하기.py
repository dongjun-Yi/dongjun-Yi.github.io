from collections import deque
# 세로, 가로, 입력받을 영역의 개수
m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for _ in range(k):
  left_x, left_y, right_x, right_y = map(int, input().split())
  for i in range(left_y, right_y):
    for j in range(left_x, right_x):
      graph[i][j] += 1

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
  q = deque([(x, y)])
  cnt = 1

  while q:
    # 가로, 세로
    y, x = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[ny][nx] == 0:
        graph[ny][nx] = 1
        q.append((ny, nx))
        cnt += 1
  return cnt


result = []

for i in range(m):
  for j in range(n):
    if graph[i][j] == 0:
      graph[i][j] = 1
      result.append(bfs(i, j))

print(len(result))

result.sort()

print(*result)
