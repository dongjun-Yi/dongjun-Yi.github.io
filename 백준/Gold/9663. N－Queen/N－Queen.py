n = int(input())

ans = 0
row = [0] * n

visited = [False] * n


def check(x):
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
      return False
  return True


def dfs(x):
  global ans
  if x == n:
    ans += 1
    return

  else:
    for i in range(n):
      if visited[i]:
        continue
      # [x, i]에 퀸을 놓겠다. x행, i열
      row[x] = i
      if check(x):
        # 재귀는 행에 맞춰서 증가. 행에 놓을 위치 결정
        visited[i] = True
        dfs(x + 1)
        visited[i] = False


dfs(0)
print(ans)
