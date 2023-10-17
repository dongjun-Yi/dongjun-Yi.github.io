from collections import deque

n, k = map(int, input().split())

s = [i for i in range(1, n + 1)]

s = deque(s)

res = []
while s:
  for _ in range(k - 1):
    s.append(s.popleft())
  res.append(s.popleft())

print("<", end='')
for i in range(len(res)):
  if i == (len(res) - 1):
    print("%d" % (res[i]), end='')
    break
  print("%d," % (res[i]), end=' ')

print(">", end='')
