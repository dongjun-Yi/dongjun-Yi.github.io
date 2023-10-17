def dfs(L, s):
  if L == 6:
    for x in res:
      print(x, end=' ')
    print()
    return
  else:
    for i in range(s, len(arr)):
      res[L] = arr[i]
      dfs(L + 1, i + 1)


while True:
  arr = list(map(int, input().split()))
  n = arr.pop(0)
  visited = [False] * (n + 1)
  res = [0] * 6
  if n == 0:
    break
  dfs(0, 0)
  print()