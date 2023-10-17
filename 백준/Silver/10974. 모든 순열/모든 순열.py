n = int(input())

visited = [False] * (n + 1)
res = [0] * n


def dfs(L):
  if L == n:
    for x in res:
      print(x, end=' ')
    print()
    return
  else:
    for i in range(1, n + 1):
      if not visited[i]:
        visited[i] = True
        res[L] = i
        dfs(L + 1)
        visited[i] = False


dfs(0)