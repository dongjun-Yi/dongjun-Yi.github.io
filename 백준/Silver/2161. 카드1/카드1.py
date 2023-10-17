from collections import deque

n = int(input())
q = deque(list(range(1, n + 1)))

res = []

while q:
  if len(q) == 1:
    break
  cur = q.popleft()
  res.append(cur)
  q.append(q.popleft())

res.append(q.popleft())

for x in res:
  print(x, end=' ')
