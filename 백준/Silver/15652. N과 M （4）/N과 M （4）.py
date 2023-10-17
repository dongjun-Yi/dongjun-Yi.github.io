n, m = map(int, input().split())
ch = [0] * (m)


def dfs(L, start):
  if L == m:
    for x in ch:
      print(x, end=' ')
    print()
  else:
    for i in range(start, n + 1):
      ch[L] = i
      dfs(L + 1, i)


dfs(0, 1)
