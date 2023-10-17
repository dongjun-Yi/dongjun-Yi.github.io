import sys

n = int(input())
foods = []
for _ in range(n):
  a, b = map(int, input().split())
  foods.append((a, b))

res = sys.maxsize


def dfs(L, sum1, sum2):
  global res

  if L == n:
    if sum1 == 1 and sum2 == 0:
      return
    if res > abs(sum1 - sum2):
      res = abs(sum1 - sum2)

  else:
    dfs(L + 1, sum1 * foods[L][0], sum2 + foods[L][1])
    dfs(L + 1, sum1, sum2)


if n == 1:
  print(abs(foods[0][0] - foods[0][1]))
else:
  dfs(0, 1, 0)
  print(res)
