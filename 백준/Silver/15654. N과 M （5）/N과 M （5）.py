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
    for i in range(n):
      if not visited[i]:
        res[L] = a[i]
        visited[i] = True
        dfs(L + 1, a[i])
        visited[i] = False


dfs(0, 0)
