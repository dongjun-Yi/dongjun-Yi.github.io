n, m = map(int, input().split())
a = list(map(int, input().split()))

res = [0] * m
visited = [False] * n

a.sort()


def dfs(L, x):
  if L == m:
    for y in res:
      print(y, end=' ')
    print()
  else:
    for i in range(x, n):
      res[L] = a[i]
      dfs(L + 1, i + 1)


dfs(0, 0)
