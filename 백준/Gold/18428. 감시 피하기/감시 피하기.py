n = int(input())

graph = []
teacher = []

for i in range(n):
  graph.append(list(input().split()))
  for j in range(n):
    if graph[i][j] == 'T':
      teacher.append((i, j))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = False


def bfs():
  for t in teacher:
    for i in range(4):
      nx, ny = t
      while True:
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
          break
        if graph[nx][ny] == 'O':
          break
        # 학생이 보이면 실패
        if graph[nx][ny] == 'S':
          return False
        nx += dx[i]
        ny += dy[i]
  return True


# 장애물 설치
def makeWall(cnt):
  global flag
  if cnt == 3:
    if bfs():
      flag = True
      return
  else:
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'X':
          graph[i][j] = 'O'
          makeWall(cnt + 1)
          graph[i][j] = 'X'


makeWall(0)

if flag:
  print("YES")
else:
  print("NO")
