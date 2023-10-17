import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(str, input())))

visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def DFS(x, y):
  visited[x][y] = True
  current_color = arr[x][y]

  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]

    if (0 <= nx < n) and (0 <= ny < n):
      if visited[nx][ny]==False:
          if arr[nx][ny] == current_color:
              DFS(nx,ny)


for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      DFS(i, j)
      cnt += 1

for i in range(n):
  for j in range(n):
    if arr[i][j] == 'R':
      arr[i][j] = 'G'

visited = [[False] * n for _ in range(n)]
two_cnt = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      DFS(i, j)
      two_cnt += 1

print(cnt, two_cnt)
