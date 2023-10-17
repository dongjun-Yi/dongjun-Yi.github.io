import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
up = [1] * n
down = [0] * n

for i in range(n):
  for j in range(i):
    if s[i] > s[j]:
      up[i] = max(up[i], up[j] + 1)

for i in range(n - 1, -1, -1):
  for j in range(i, n):
    if s[i] > s[j]:
      down[i] = max(down[i], down[j] + 1)

sum = 0

for i in range(n):
  sum = max(sum, up[i] + down[i])

print(sum)
