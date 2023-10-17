graph = []
for i in range(9):
  graph.append(list(map(int, input().split())))

blank = []
for i in range(9):
  for j in range(9):
    if graph[i][j] == 0:
      blank.append((i, j))


def checkRow(x, a):
  for i in range(9):
    if graph[x][i] == a:
      return False
  return True


def checkCol(y, a):
  for i in range(9):
    if graph[i][y] == a:
      return False
  return True


def checkRect(x, y, a):
  nx = (x // 3) * 3
  ny = (y // 3) * 3

  for i in range(3):
    for j in range(3):
      if graph[nx + i][ny + j] == a:
        return False
  return True


def dfs(index):
  if index == len(blank):
    for i in range(9):
      for j in range(9):
        print(graph[i][j], end=' ')
      print()
    exit()
  else:
    for i in range(1, 10):
      x = blank[index][0]
      y = blank[index][1]

      if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
        graph[x][y] = i
        dfs(index + 1)
        graph[x][y] = 0


dfs(0)
