import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dy = [0] * (k + 1)

for i in range(n):
  w, v = map(int, input().split())
  for j in range(k, w-1, -1):
    dy[j] = max(dy[j], dy[j - w] + v)

print(dy[k])
