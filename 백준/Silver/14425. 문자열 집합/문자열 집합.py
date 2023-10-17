import sys

input = sys.stdin.readline

s = set()
n, m = map(int, input().split())

for _ in range(n):
  data = input().rstrip()
  s.add(data)

cnt = 0

for _ in range(m):
  data = input().rstrip()
  if data in s:
    cnt += 1

print(cnt)
