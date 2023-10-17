n, m = map(int, input().split())
ch = [0] * (m)


def dfs(L):
  if L == m:
    for x in ch:
      print(x, end=' ')
    print()
  else:
    for i in range(1, n + 1):
      ch[L] = i
      dfs(L + 1)


dfs(0)