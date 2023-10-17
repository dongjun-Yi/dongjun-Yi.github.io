import sys

input = sys.stdin.readline
n, x = map(int, input().split())

visiters = list(map(int, input().split()))

tmp = sum(visiters[:x])
res = tmp
cnt = 1

# 슬라이딩 윈도우, O(n)
for i in range(x, n):
  tmp -= visiters[i - x]
  tmp += visiters[i]
  if tmp > res:
    res = tmp
    cnt = 1
  elif tmp == res:
    cnt += 1

if res == 0:
  print("SAD")
else:
  print(res)
  print(cnt)
