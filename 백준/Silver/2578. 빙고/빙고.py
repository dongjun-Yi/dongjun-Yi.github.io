import sys

board = []
for _ in range(5):
  board.append(list(map(int, input().split())))

visited = [[False] * 5 for _ in range(5)]


def check_row():
  row_cnt = 0
  for i in range(5):
    if all(visited[i]):
      row_cnt += 1

  return row_cnt


def check_col():
  col_cnt = 0

  for i in range(5):
    tmp = 0
    for j in range(5):
      if visited[j][i]:
        tmp += 1
    if tmp == 5:
      col_cnt += 1
  return col_cnt


def check_leftdig():
  leftdig_cnt = 0
  for i in range(5):
    if visited[i][i]:
      leftdig_cnt += 1
  if leftdig_cnt == 5:
    return 1
  else:
    return 0


def check_rightdig():
  rightdig_cnt = 0

  for i in range(5):
    if visited[i][4 - i]:
      rightdig_cnt += 1
  if rightdig_cnt == 5:
    return 1
  else:
    return 0


c = 0
ans = sys.maxsize

for _ in range(5):
  a = list(map(int, input().split()))

  for x in a:
    c += 1
    for i in range(5):
      for j in range(5):
        if x == board[i][j]:
          visited[i][j] = True

        res = check_row() + check_col() + check_leftdig() + check_rightdig()
        if res >= 3:
          ans = min(c, ans)

print(ans)
