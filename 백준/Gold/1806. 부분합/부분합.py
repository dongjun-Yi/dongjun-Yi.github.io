import sys

n, s = map(int, input().split())

a = list(map(int, input().split()))

lt, rt = 0, 0
res = sys.maxsize
tmp = a[lt]

while True:
  if tmp >= s:
    res = min(res, rt - lt + 1)
    tmp -= a[lt]
    lt += 1
  else:
    rt += 1
    if rt == n:
      break
    tmp += a[rt]

print(0) if res == sys.maxsize else print(res)
