from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

# 상, 하 ,좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 15 and ny < 15 and nx >= 0 and ny >= 0 and graph[x][y] == 0:
        x = nx
        y = ny
        graph[x][y] = 1
        queue.append((x, y))
  return True


for i in range(n):
  for j in range(m):
    if bfs(i, j) == True:
      print(i, j)
      result += 1
