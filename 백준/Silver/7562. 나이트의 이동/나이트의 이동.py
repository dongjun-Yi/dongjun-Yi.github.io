from collections import deque

t = int(input())

moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2),
         (-1, -2)]


def bfs(x, y):
  q = deque([(x, y)])

  while q:
    cur = q.popleft()

    if cur[0] == tarx and cur[1] == tary:
      return graph[tarx][tary]

    for i in range(len(moves)):
      dx, dy = moves[i]
      nx = cur[0] + dx
      ny = cur[1] + dy

      if nx < 0 or nx >= l or ny < 0 or ny >= l:
        continue

      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[cur[0]][cur[1]] + 1
        q.append((nx, ny))


for _ in range(t):
  l = int(input())
  graph = [[0] * l for _ in range(l)]
  curx, cury = map(int, input().split())
  tarx, tary = map(int, input().split())
  print(bfs(curx, cury))
